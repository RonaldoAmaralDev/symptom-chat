import redis
import requests
import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.core import config
from app.models.agent import Agent

r = config.redis_client

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Você é um assistente virtual de saúde. "
        "Seu papel é acolher o usuário, perguntar primeiro o nome (ou nome social) e a idade, "
        "se ainda não foram informados. "
        "Depois disso, peça para descrever os sintomas (ex.: dor de cabeça, fadiga, febre, dor no peito, falta de ar, etc). "
        "Seja empático, claro e profissional. "
        "Sempre pergunte detalhes relevantes sobre os sintomas (há quanto tempo sente, intensidade, fatores que pioram ou aliviam). "
        "Forneça apenas dicas gerais de cuidado (hidratação, repouso, observar sinais de alerta). "
        "Nunca dê diagnósticos ou prescreva medicamentos. "
        "Sempre enfatize que o mais recomendado é procurar atendimento médico imediato em um posto de saúde ou hospital, "
        "especialmente se os sintomas forem fortes, persistentes ou preocupantes. "
        "Use linguagem acessível, mas séria e respeitosa, sem piadas ou ironias. "
        "Após o usuário prescrever os sintomas, perguntar se já foi ao atendimento médico, se sim sugerir para ele entrar na aba de receita médica."
    ),
}


async def get_agent(session: AsyncSession, agent_id: int) -> Agent:
    """Busca agente ativo no banco"""
    result = await session.execute(select(Agent).where(Agent.id == agent_id))
    agent = result.scalar_one_or_none()
    if not agent or not agent.enabled:
        raise HTTPException(status_code=400, detail="Agente inválido ou inativo")
    return agent


def build_messages(session_id: str, message: str):
    """Monta histórico + mensagem atual"""
    history_key = f"chat:{session_id}:history"
    history = r.lrange(history_key, 0, -1)
    history = [h.decode("utf-8") for h in history]

    r.rpush(history_key, f"user: {message}")

    messages = [SYSTEM_PROMPT]
    for h in history:
        role, text = h.split(":", 1)
        messages.append({"role": role.strip(), "content": text.strip()})
    messages.append({"role": "user", "content": message})

    return history_key, messages


def stream_ollama(agent: Agent, messages, history_key: str):
    """Chamada para Ollama (local) - síncrona"""
    with requests.post(
        f"{config.OLLAMA_URL}/api/chat",
        json={"model": "llama3.2:3b", "messages": messages},
        stream=True,
        timeout=60,
    ) as resp:
        if resp.status_code != 200:
            yield f"data: [Erro ao conectar ao Ollama: {resp.status_code}]\n\n"
            return

        full_answer, buffer = "", ""
        for line in resp.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                token = data.get("message", {}).get("content", "")
                if not token:
                    continue

                buffer += token
                if buffer.endswith((" ", ".", ",", "!", "?", ";", ":", "…")):
                    yield f"data: {buffer}\n\n"
                    full_answer += buffer
                    buffer = ""
            except Exception:
                continue

        if buffer:
            yield f"data: {buffer}\n\n"
            full_answer += buffer

        r.rpush(history_key, f"assistant: {full_answer}")


async def chat_stream(session: AsyncSession, session_id: str, message: str, agent_id: int):
    agent = await get_agent(session, agent_id)
    history_key, messages = build_messages(session_id, message)

    if agent.provider == "ollama":
        for chunk in stream_ollama(agent, messages, history_key):
            yield chunk
    elif agent.provider == "openai":
        yield f"data: [OpenAI ainda não implementado]\n\n"
    else:
        yield f"data: [Provider {agent.provider} não suportado]\n\n"


def reset_session(session_id: str):
    r.delete(f"chat:{session_id}:history")
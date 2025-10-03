import redis
import requests
import json
from app.core import config

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
        "Use linguagem acessível, mas séria e respeitosa, sem piadas ou ironias."
        "Após o usuário prescrever os sintomas, perguntar se já foi ao atendimento medico, se sim sugerir para ele entrar na aba de receita médica."
    ),
}

def chat_stream(session_id: str, message: str):
    history_key = f"chat:{session_id}:history"
    history = r.lrange(history_key, 0, -1)
    history = [h.decode("utf-8") for h in history]

    r.rpush(history_key, f"user: {message}")

    messages = [SYSTEM_PROMPT]
    for h in history:
        role, text = h.split(":", 1)
        messages.append({"role": role.strip(), "content": text.strip()})
    messages.append({"role": "user", "content": message})

    with requests.post(
        f"{config.OLLAMA_URL}/api/chat",
        json={"model": "llama3.2:3b", "messages": messages},
        stream=True,
        timeout=60,
    ) as resp:
        if resp.status_code != 200:
            yield f"data: [Erro ao conectar ao modelo: {resp.status_code}]\n\n"
            return

        full_answer = ""
        buffer = ""

        for line in resp.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                token = data.get("message", {}).get("content", "")
                if not token:
                    continue

                buffer += token

                # Solta quando há indício de palavra completa
                if buffer.endswith((" ", ".", ",", "!", "?", ";", ":", "…")):
                    yield f"data: {buffer}\n\n"
                    full_answer += buffer
                    buffer = ""

            except Exception:
                continue

        # Flush final (se sobrou coisa no buffer)
        if buffer:
            yield f"data: {buffer}\n\n"
            full_answer += buffer

        r.rpush(history_key, f"assistant: {full_answer}")


def reset_session(session_id: str):
    r.delete(f"chat:{session_id}:history")
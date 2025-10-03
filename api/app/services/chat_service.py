import redis
import requests
from app.core import config

r = config.redis_client

def chat_with_ai(session_id: str, message: str) -> str:
    """
    Mantém histórico no Redis e chama Ollama para responder.
    """
    # Recupera histórico da sessão
    history_key = f"chat:{session_id}:history"
    history = r.lrange(history_key, 0, -1)
    history = [h.decode("utf-8") for h in history]

    # Adiciona a nova mensagem do usuário
    r.rpush(history_key, f"user: {message}")

    # Prepara prompt simples (pode ser melhorado com RAG + Chroma)
    prompt = "\n".join(history) + f"\nassistant:"

    # Chama Ollama
    try:
        resp = requests.post(
            f"{config.OLLAMA_URL}/api/generate",
            json={"model": "llama3.2:3b", "prompt": prompt},
            timeout=30,
        )
        data = resp.json()
        answer = data.get("response", "Desculpe, não consegui gerar uma resposta.")
    except Exception as e:
        answer = f"Erro ao conectar ao modelo: {e}"

    # Salva resposta no histórico
    r.rpush(history_key, f"assistant: {answer}")

    return answer

def reset_session(session_id: str):
    history_key = f"chat:{session_id}:history"
    r.delete(history_key)

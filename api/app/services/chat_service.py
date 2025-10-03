import redis
import requests
import json
from app.core import config

r = config.redis_client

def chat_stream(session_id: str, message: str):
    """
    Gera resposta do modelo em streaming, mas junta tokens parciais
    para evitar palavras quebradas (ex: 'Ol á' -> 'Olá').
    """
    history_key = f"chat:{session_id}:history"
    history = r.lrange(history_key, 0, -1)
    history = [h.decode("utf-8") for h in history]

    r.rpush(history_key, f"user: {message}")

    messages = []
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

                if buffer.endswith((" ", ".", ",", "!", "?", ";", ":", '"', "'", ")", "(", "…")):
                    full_answer += buffer
                    yield f"data: {buffer}\n\n"
                    buffer = ""

            except Exception:
                continue

        if buffer:
            full_answer += buffer
            yield f"data: {buffer}\n\n"

        r.rpush(history_key, f"assistant: {full_answer}")


def reset_session(session_id: str):
    r.delete(f"chat:{session_id}:history")
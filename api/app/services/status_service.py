import requests
from app.core import config

def check_status():
    status_info = {
        "api": "ok",
        "redis": False,
        "chroma": False,
        "ollama": False,
    }

    # Redis
    try:
        config.redis_client.ping()
        status_info["redis"] = True
    except Exception:
        pass

    # Chroma
    try:
        resp = requests.get(f"{config.CHROMA_URL}/api/v1/heartbeat", timeout=2)
        if resp.status_code == 200:
            status_info["chroma"] = True
    except Exception:
        pass

    # Ollama
    try:
        resp = requests.get(f"{config.OLLAMA_URL}/api/tags", timeout=2)
        if resp.status_code == 200:
            status_info["ollama"] = True
    except Exception:
        pass

    return status_info

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import requests

app = FastAPI(title="Symptom Chat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_URL = "redis://redis:6379/0"
CHROMA_URL = "http://chroma:8000"
OLLAMA_URL = "http://ollama:11434"

r = redis.Redis.from_url(REDIS_URL)

@app.get("/status")
def status():
    status_info = {
        "api": "ok",
        "redis": False,
        "chroma": False,
        "ollama": False,
    }

    # Testa Redis
    try:
        r.ping()
        status_info["redis"] = True
    except Exception:
        status_info["redis"] = False

    # Testa Chroma
    try:
        resp = requests.get(f"{CHROMA_URL}/api/v1/heartbeat", timeout=2)
        if resp.status_code == 200:
            status_info["chroma"] = True
    except Exception:
        status_info["chroma"] = False

    # Testa Ollama
    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2)
        if resp.status_code == 200:
            status_info["ollama"] = True
    except Exception:
        status_info["ollama"] = False

    return status_info
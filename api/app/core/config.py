import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
CHROMA_URL = os.getenv("CHROMA_URL", "http://chroma:8000")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")

redis_client = redis.Redis.from_url(REDIS_URL)
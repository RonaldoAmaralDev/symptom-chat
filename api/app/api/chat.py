from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import chat_stream, reset_session
from app.core import config
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

r = config.redis_client
router = APIRouter()

@router.post("/chat/stream")
def chat(req: ChatRequest, session: AsyncSession = Depends(get_db)):
    return StreamingResponse(
        chat_stream(session, req.session_id, req.message, req.agent_id),
        media_type="text/event-stream"
    )

@router.delete("/session/{session_id}")
def reset(session_id: str):
    reset_session(session_id)
    return {"status": "reset"}

@router.get("/session/{session_id}")
def get_session(session_id: str):
    history_key = f"chat:{session_id}:history"
    history = r.lrange(history_key, 0, -1)
    history = [h.decode("utf-8") for h in history]

    messages = []
    for h in history:
        role, text = h.split(":", 1)
        messages.append({
            "role": role.strip(),
            "content": text.strip()
        })

    return {"messages": messages}
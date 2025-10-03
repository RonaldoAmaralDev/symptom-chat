from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import chat_stream, reset_session

router = APIRouter()

@router.post("/chat/stream")
def chat(req: ChatRequest):
    """
    Retorna resposta em streaming (SSE).
    """
    return StreamingResponse(
        chat_stream(req.session_id, req.message),
        media_type="text/event-stream"
    )

@router.delete("/session/{session_id}")
def reset(session_id: str):
    reset_session(session_id)
    return {"status": "reset"}

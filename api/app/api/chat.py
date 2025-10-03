from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import chat_with_ai, reset_session

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer = chat_with_ai(req.session_id, req.message)
    return {"answer": answer}

@router.delete("/session/{session_id}")
def reset(session_id: str):
    reset_session(session_id)
    return {"status": "reset"}

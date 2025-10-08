from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    message: str
    agent_id: int

class ChatResponse(BaseModel):
    answer: str
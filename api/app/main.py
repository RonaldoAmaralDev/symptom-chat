from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import status, chat, agents

app = FastAPI(title="Symptom Chat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status.router, prefix="/api/v1", tags=["status"])
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])
app.include_router(agents.router, prefix="/api/v1", tags=["Agents"])

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.services.agent_service import AgentService

router = APIRouter()

@router.get("/agents")
async def list_agents(session: AsyncSession = Depends(get_db)):
    return await AgentService.list_agents(session)

@router.put("/agents/{agent_id}/toggle")
async def toggle_agent(agent_id: int, session: AsyncSession = Depends(get_db)):
    return await AgentService.toggle_agent(agent_id, session)

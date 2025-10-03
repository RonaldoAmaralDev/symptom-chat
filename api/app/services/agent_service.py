from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.models.agent import Agent


class AgentService:
    @staticmethod
    async def list_agents(session: AsyncSession):
        result = await session.execute(select(Agent))
        agents = result.scalars().all()
        return [a.as_dict() for a in agents]

    @staticmethod
    async def toggle_agent(agent_id: int, session: AsyncSession):
        result = await session.execute(select(Agent).where(Agent.id == agent_id))
        agent = result.scalar_one_or_none()

        if not agent:
            raise HTTPException(status_code=404, detail="Agente não encontrado")

        agent.enabled = not agent.enabled
        await session.commit()
        await session.refresh(agent)

        return {
            "message": f"Agente {'ativado' if agent.enabled else 'desativado'} com sucesso",
            "agent": agent.as_dict(),
        }
    
    @staticmethod
    async def update_agent(agent_id: int, data: dict, session: AsyncSession):
        result = await session.execute(select(Agent).where(Agent.id == agent_id))
        agent = result.scalar_one_or_none()

        if not agent:
            raise HTTPException(status_code=404, detail="Agente não encontrado")

        for field in ["name", "provider", "api_key", "config", "logo_url", "enabled"]:
            if field in data:
                setattr(agent, field, data[field])

        await session.commit()
        await session.refresh(agent)

        return {
            "message": "Agente atualizado com sucesso",
            "agent": agent.as_dict(),
        }

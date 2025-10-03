import asyncio
from sqlalchemy.future import select
from app.db import AsyncSessionLocal
from app.models.agent import Agent

AGENTS = [
    {
        "name": "Ollama",
        "provider": "ollama",
        "enabled": True,
        "api_key": None,
        "config": {"model": "llama3"},
        "logo_url": "https://ollama.com/public/ollama.png",
    },
    {
        "name": "OpenAI GPT-4o",
        "provider": "openai",
        "enabled": False,
        "api_key": None,
        "config": {"model": "gpt-4o"},
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg",
    },
    {
        "name": "Anthropic Claude",
        "provider": "anthropic",
        "enabled": False,
        "api_key": None,
        "config": {"model": "claude-3-opus"},
        "logo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEWg2jpoNSbc2mR0reo-ANwwuCOog6NcmAJA&s",
    },
    {
        "name": "Mistral AI",
        "provider": "mistral",
        "enabled": False,
        "api_key": None,
        "config": {"model": "mistral-large"},
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Mistral_AI_logo_%282025%E2%80%93%29.svg/1200px-Mistral_AI_logo_%282025%E2%80%93%29.svg.png",
    },
    {
        "name": "Google Gemini",
        "provider": "google",
        "enabled": False,
        "api_key": None,
        "config": {"model": "gemini-1.5-pro"},
        "logo_url": "https://www.gstatic.com/lamda/images/gemini_aurora_thumbnail_4g_e74822ff0ca4259beb718.png",
    },
    {
        "name": "Meta LLaMA",
        "provider": "meta",
        "enabled": False,
        "api_key": None,
        "config": {"model": "llama3-70b"},
        "logo_url": "https://store-images.s-microsoft.com/image/apps.22898.a77ddd81-b691-40b6-98f4-ea554a15e8d1.6f8a7ba6-a2d9-4877-91c6-49e3bbe0f123.30aac663-23af-4d74-b0fa-0e37e733d772",
    },
    {
        "name": "Cohere Command R+",
        "provider": "cohere",
        "enabled": False,
        "api_key": None,
        "config": {"model": "command-r-plus"},
        "logo_url": "https://avatars.githubusercontent.com/u/59763961?s=200&v=4",
    },
    {
        "name": "xAI Grok",
        "provider": "xai",
        "enabled": False,
        "api_key": None,
        "config": {"model": "grok-1.5"},
        "logo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTc_zzAUCC7sHMf_d8hqXnQW29EI_eBXPbiQ&s",
    },
]

async def seed_agents():
    async with AsyncSessionLocal() as session:
        for data in AGENTS:
            result = await session.execute(
                select(Agent).where(Agent.name == data["name"])
            )
            existing = result.scalar_one_or_none()
            if not existing:
                agent = Agent(**data)
                session.add(agent)
                print(f"✅ Criado agente: {data['name']}")
            else:
                print(f"⚠️ Já existe: {data['name']}")
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed_agents())

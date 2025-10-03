from sqlalchemy import Column, Integer, String, Boolean, Text, JSON, DateTime, func
from app.db import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    provider = Column(String(100), nullable=False)
    enabled = Column(Boolean, default=False)
    api_key = Column(Text, nullable=True)
    config = Column(JSON, nullable=True)
    logo_url = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "provider": self.provider,
            "enabled": self.enabled,
            "api_key": self.api_key,
            "config": self.config,
            "logo_url": self.logo_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

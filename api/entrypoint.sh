#!/bin/sh
set -e

echo "⏳ Aguardando banco ficar pronto..."
sleep 5

echo "🚀 Rodando migrations..."
alembic upgrade head

echo "🌱 Rodando seeds..."
python -m app.scripts.seed_agents || true

echo "✅ Iniciando API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8088 --reload
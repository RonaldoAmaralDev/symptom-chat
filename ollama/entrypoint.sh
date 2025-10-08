#!/bin/bash
set -e

echo "🚀 Iniciando Ollama server..."
ollama serve &
sleep 5

pull_if_missing() {
  local model=$1
  if ! ollama list | grep -q "$model"; then
    echo "📦 Baixando modelo: $model..."
    ollama pull "$model"
  else
    echo "✅ Modelo $model já está instalado."
  fi
}

pull_if_missing "llama3.2:3b"
pull_if_missing "nomic-embed-text:latest"

echo "🎯 Modelos prontos. Mantendo serviço ativo..."
tail -f /dev/null

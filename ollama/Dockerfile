FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y bash curl && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["ollama serve & sleep 5 && ollama pull llama3.2:3b && ollama pull nomic-embed-text:latest && wait"]
# 🤖 RAG Symptom Chat (FastAPI + Vue + Redis + Chroma + Ollama)

> **Aviso importante:** Este projeto é apenas para **informação** e **educação**. Não fornece diagnóstico nem prescrição. Sempre consulte um médico.

---

## 📦 Stack
- **Backend:** FastAPI + LangChain + ChromaDB + Redis
- **Frontend:** Vue 3 + Vite + Tailwind + Chart.js
- **LLM:** Ollama (Llama 3.x)
- **Infra:** Docker Compose (WSL2)

---

## ▶️ Como rodar

### 1. Clonar projeto
```bash
git clone <repo>
cd rag-symptom-chat
```

### 2. Subir containers
```bash
docker compose up -d --build
```

### 3. Baixar modelos no Ollama
```bash
✅ Os modelos **llama3.2:3b (~3.8GB)** e **nomic-embed-text** já são baixados automaticamente no `docker compose up`.
```

### 4. Acessar
- **Chat:** [http://localhost:5173](http://localhost:5173)  
- **Dashboard:** [http://localhost:5173/dashboard](http://localhost:5173/dashboard)  
- **Receita Médica:** [http://localhost:5173/receita](http://localhost:5173/receita)  

---

## 💬 Funcionalidades

### Chat
- Conversa em tempo real (WebSocket)
- Sugestões de **produtos** e **ações**
- Detecção de **red flags**
- Exibição de **fontes consultadas**
- Botão **Resetar conversa**

### Dashboard
- Perguntas mais feitas
- Produtos mais sugeridos
- Tempo médio de resposta
- Quantidade de erros
- Custos de transação
- Gráficos com Chart.js (barras, linha)

### Receita Médica
- Upload de imagem/PDF da receita
- OCR com Tesseract
- Explicação dos medicamentos prescritos
- Sugestão de próximos passos (cuidados, onde comprar)

---

## 🚀 Melhorias futuras
- Exportar métricas em CSV/Excel
- Mais integrações no módulo de receita (farmácias online, APIs médicas)
- Alertas customizados por paciente
- Agendamento médico direto pelo sistema

---

## ⚡ Notas
- Desenvolvido para rodar no **WSL2 + Docker**.
- Backend em **Python 3.11**, Frontend em **Node 20**.
- Recomendado ter pelo menos **8GB de RAM** disponível para Ollama + Chroma.


# 🤖 Symptom Chat – RAG com FastAPI + Vue + Ollama + Redis + Chroma

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Vue](https://img.shields.io/badge/Vue-3.x-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Redis](https://img.shields.io/badge/Redis-7-red)
![Chroma](https://img.shields.io/badge/ChromaDB-RAG-orange)

Chat inteligente que interpreta **sintomas** e sugere **ações/produtos** usando **RAG (Retrieval Augmented Generation)** com **Llama 3.2 (3B)** rodando no **Ollama**.

> ⚠️ Este projeto é apenas **educacional**. Não fornece diagnóstico médico.

---

## 🚀 Como rodar com Docker (WSL2)

```bash
git clone https://github.com/RonaldoAmaralDev/symptom-chat.git
cd symptom-chat
cp api/.env.example api/.env
docker compose up --build
```

👉 O navegador deve ser aberto em: **http://localhost:5173**

---

## 📚 Funcionalidades

### 💬 Chat
- Conversa em tempo real (WebSocket)
- Memória persistida no Redis
- Sugestões de **produtos** e **ações**
- Detecção de **red flags**
- Exibição de **fontes consultadas**
- Botão **Resetar conversa**

### 📊 Dashboard
- Perguntas mais feitas
- Produtos mais sugeridos
- Tempo médio de resposta
- Quantidade de erros
- Custos de transação
- Gráficos com **Chart.js** (barras + linhas)

### 📄 Receita Médica
- Upload de imagem/PDF da receita
- OCR com **Tesseract**
- Explicação dos medicamentos prescritos
- Sugestão de próximos passos (cuidados, onde comprar)

---

## 🛠️ Stack

- **Backend:** FastAPI + LangChain + Redis + ChromaDB  
- **Frontend:** Vue 3 + Vite + Tailwind + Chart.js  
- **LLM:** Ollama (Llama 3.2 3B, ~3.8GB)  
- **Infra:** Docker Compose (WSL2/Linux)  

---

## 🗺 Melhorias Futuras

- Exportar métricas em CSV/Excel  
- Integração com APIs de farmácias  
- Alertas customizados por paciente  
- Agendamento médico integrado  

---

## 📸 Screenshots (em breve)

- Chat em tempo real  
- Dashboard com métricas  
- Receita médica analisada  

---

## ✨ Autor

Desenvolvido por [**Ronaldo Amaral**](https://github.com/RonaldoAmaralDev) 🚀
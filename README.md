
# 🤖 Symptom Chat – RAG com FastAPI + Vue + Ollama + Redis + Chroma

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Vue](https://img.shields.io/badge/Vue-3.x-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Redis](https://img.shields.io/badge/Redis-7-red)
![Chroma](https://img.shields.io/badge/ChromaDB-RAG-orange)

Plataforma interativa de **atendimento de sintomas via IA**, que utiliza **RAG (Retrieval Augmented Generation)** com **Ollama (Llama 3.2 3B)** para gerar respostas contextualizadas e seguras.

> ⚠️ Projeto de caráter **educacional**. Não realiza diagnósticos médicos reais.

---

## 🚀 Como rodar com Docker (WSL2)

```bash
git clone https://github.com/RonaldoAmaralDev/symptom-chat.git
cd symptom-chat
cp api/.env.example api/.env
cp frontend/.env.example frontend/.env
docker compose up --build
```

👉 Acesse no navegador: **http://localhost:5173**

---

## 📚 Funcionalidades

### 💬 Bate-papo com Agente Dinâmico
- Comunicação em **tempo real** (streaming SSE)  
- **Memória persistente** via Redis  
- Seleção dinâmica de **agentes** (ex.: saúde, nutrição, bem-estar)  
- Respostas personalizadas com base no agente selecionado  
- Detecção de termos críticos (“red flags”)  
- Sugestões automáticas de **ações** e **produtos**

### 🧩 CRUD de Agentes
- Criação, edição, listagem e exclusão de agentes  
- Configuração de parâmetros (modelo, provider, descrição, status)  
- Integração direta com o chat dinâmico  
- Persistência via FastAPI + SQLAlchemy + Postgres  

---

## 🧠 Próximas Features

### 📊 Dashboard
- Indicadores de conversas, agentes e tempo de resposta  
- Análise de engajamento e custo por interação  
- Visualizações com **Chart.js** (linhas, barras e radar)

### 🧾 Scanner de Receita Médica
- Upload de imagens/PDFs de receitas  
- OCR com **Tesseract**  
- Interpretação dos medicamentos prescritos  
- Sugestões de cuidados e locais de compra  

---

## 🧱 Arquitetura do Projeto

```
              ┌──────────────────┐
              │     Frontend     │
              │  (Vue + Vite)    │
              └──────┬───────────┘
                     │
     HTTP / SSE      │
                     ▼
              ┌──────────────────┐
              │     FastAPI      │
              │  (Chat + CRUD)   │
              └──────┬───────────┘
        ┌────────────┼───────────────┐
        ▼            ▼               ▼
   ┌────────┐   ┌──────────┐   ┌──────────┐
   │ Redis  │   │ ChromaDB │   │ Postgres │
   └────────┘   └──────────┘   └──────────┘
                     │
                     ▼
              ┌──────────────────┐
              │     Ollama       │
              │ (Llama 3.2 3B)   │
              └──────────────────┘
```

---

## 📁 Estrutura de Pastas

```
symptom-chat/
├── api/                      # Backend FastAPI
│   ├── app/                  # Código principal (models, services, routes)
│   ├── alembic/              # Migrations
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/                 # Aplicação Vue 3
│   ├── src/                  # Componentes, views e store
│   ├── public/
│   ├── Dockerfile
│   └── .env.example
│
├── ollama/                   # Configuração do servidor Ollama
│   ├── Dockerfile
│   └── entrypoint.sh
│
├── docker-compose.yml        # Orquestração dos serviços
├── README.md
└── LICENSE
```

---

## 🛠️ Stack

- **Backend:** FastAPI • SQLAlchemy • Redis • ChromaDB  
- **Frontend:** Vue 3 • Vite • Pinia • TailwindCSS  
- **LLM / IA:** Ollama (Llama 3.2 3B)  
- **Infra:** Docker Compose (WSL2 / Linux)  

---

## 🗺️ Melhorias Futuras

- Exportação de métricas (CSV/Excel)  
- Integração com APIs de farmácias  
- Alertas e histórico por paciente  
- Agendamento de atendimentos via IA  

---

## 📸 Screenshots (em breve)

- Interface do chat dinâmico  
- CRUD de agentes  
- Dashboard e análise de receitas médicas  

---

## ✨ Autor

Desenvolvido por [**Ronaldo Amaral**](https://github.com/RonaldoAmaralDev) 🚀  
Explorando IA generativa, RAG e agentes autônomos com foco em aplicações práticas e seguras.
# Customer Support AI Agent

> **Business Use Case:** SaaS & E-commerce Tier-1 Support Automation

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) ![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)

## Overview

A production-ready RAG (Retrieval-Augmented Generation) based AI customer support agent. Ingests your company's documentation, FAQs, and knowledge base, then answers customer queries with source citations. Automatically escalates unresolved queries to human agents.

**Business Impact:** Reduces Tier-1 support costs by 60-80%, handles unlimited concurrent conversations, and operates 24/7 without fatigue.

## Features

- **RAG Architecture** — Answers grounded in your actual documentation
- **Multi-source Ingestion** — PDFs, web pages, Notion, Confluence, Google Docs
- **Citation Support** — Every answer includes source references
- **Smart Escalation** — Detects frustration, complexity, and routes to humans
- **Conversation Memory** — Remembers context across multi-turn conversations
- **Multi-channel** — Web widget, Slack bot, WhatsApp integration
- **Analytics Dashboard** — Query volume, resolution rate, satisfaction scores
- **A/B Testing** — Compare different prompt strategies

## Tech Stack

| Layer | Technology |
|-------|------------|
| LLM | GPT-4o / Claude 3.5 Sonnet |
| RAG Framework | LangChain + LlamaIndex |
| Vector Store | ChromaDB / Pinecone |
| Embeddings | OpenAI text-embedding-3-small |
| Backend | FastAPI + WebSockets |
| Frontend | React + Tailwind CSS |
| Database | PostgreSQL (conversation history) |
| Cache | Redis (session management) |

## Architecture

```
Documents (PDF/Web/Notion)
        ↓
  [Ingestion Pipeline]
        ↓
  [Chunking + Embedding]
        ↓
  [Vector Store (ChromaDB)]
        ↓
User Query → [Retrieval] → [LLM (GPT-4o)] → Response + Citations
                                    ↓
                          [Escalation Detector]
                                    ↓
                          Human Agent (if needed)
```

## Project Structure

```
customer-support-ai-agent/
├── backend/
│   ├── main.py
│   ├── ingestion/
│   │   ├── document_loader.py   # Multi-source ingestion
│   │   ├── chunker.py           # Smart text chunking
│   │   └── embedder.py          # Embedding generation
│   ├── rag/
│   │   ├── retriever.py         # Hybrid search retrieval
│   │   ├── chain.py             # LangChain RAG chain
│   │   └── memory.py            # Conversation memory
│   ├── agent/
│   │   ├── escalation.py        # Escalation detection
│   │   └── router.py            # Query routing logic
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── ChatWidget.jsx
│       └── AnalyticsDashboard.jsx
├── docker-compose.yml
└── README.md
```

## Setup & Installation

```bash
git clone https://github.com/nkhalfe56-star/customer-support-ai-agent
cd customer-support-ai-agent
cd backend && pip install -r requirements.txt
export OPENAI_API_KEY=your_key
uvicorn main:app --reload
```

## Business Case

| Metric | Human Support | AI Agent |
|--------|--------------|----------|
| Cost per ticket | $8-15 | $0.02-0.05 |
| Response time | 4-24 hours | < 3 seconds |
| Availability | Business hours | 24/7/365 |
| Concurrent chats | 1 per agent | Unlimited |
| Consistency | Variable | 100% |

## License

MIT License

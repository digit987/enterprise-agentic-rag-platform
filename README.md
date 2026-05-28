# Enterprise Agentic RAG Platform

A production-style Agentic Retrieval-Augmented Generation (RAG) platform featuring hybrid retrieval, graph-based multi-agent orchestration, conversational memory, tool-calling agents, observability pipelines, and web-augmented reasoning workflows.

---

# Overview

This project implements an enterprise-oriented AI assistant architecture capable of:

* semantic document retrieval,
* conversational question answering,
* hybrid search,
* multi-tool orchestration,
* conversational memory,
* evaluation and observability,
* live web search augmentation.

The system combines FastAPI, LangGraph, PostgreSQL, Qdrant, OpenAI APIs, and multi-agent workflows to simulate production-style AI engineering systems.

---

# Features

## Retrieval-Augmented Generation (RAG)

* Dense vector retrieval using OpenAI embeddings
* Qdrant vector database integration
* PostgreSQL metadata persistence
* PDF ingestion and chunking pipelines

---

## Hybrid Retrieval Pipeline

* Semantic vector search
* BM25 keyword retrieval
* CrossEncoder reranking
* Metadata-aware retrieval workflows

---

## Agentic AI Workflows

Implemented using LangGraph orchestration:

* Planner Agent
* Router Agent
* Retrieval Agent
* Verification Agent
* Response Generation Agent
* Tool Execution Agent

---

## Conversational Memory

* Session-based memory persistence
* Multi-turn conversational context
* Context-aware retrieval workflows

---

## Tool Calling

Dynamic tool-routing architecture supporting:

* Calculator Tool
* Retrieval Tool
* Web Search Tool (Tavily)

---

## Observability and Evaluation

* Token usage tracking
* Latency monitoring
* Grounding evaluation
* Retrieval evaluation
* LangSmith tracing integration

---

# System Architecture

```text
User Query
    ↓
FastAPI Backend
    ↓
LangGraph Orchestration
    ↓
Router Agent
 ├── Retrieval Tool
 ├── Calculator Tool
 └── Web Search Tool
    ↓
Hybrid Retrieval Pipeline
 ├── Qdrant Vector Search
 ├── BM25 Retrieval
 └── CrossEncoder Reranking
    ↓
LLM Response Generation
    ↓
Conversation Memory + Evaluation
```

---

# Tech Stack

## Backend

* FastAPI
* Python
* SQLAlchemy
* Docker

## Databases

* PostgreSQL
* Qdrant Vector Database

## AI/LLM Stack

* OpenAI API
* LangChain
* LangGraph
* SentenceTransformers
* BM25 Retrieval
* CrossEncoder Reranking

## Observability

* LangSmith
* RAG Evaluation Pipelines

---

# API Endpoints

## Upload PDF

```http
POST /api/v1/ingest/upload-pdf
```

Uploads and indexes PDF documents.

---

## Chat Endpoint

```http
POST /api/v1/rag/chat
```

Supports:

* conversational retrieval,
* memory-aware interactions,
* tool-calling workflows,
* web-augmented responses.

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/digit987/enterprise-agentic-rag-platform.git
cd enterprise-agentic-rag-platform
```

---

## Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

## Start Infrastructure

```bash
docker compose up -d
```

---

## Start Backend

```bash
uvicorn app.main:app --reload
```

---

# Future Improvements

* Streaming responses
* Redis caching
* Kubernetes deployment
* Authentication and RBAC
* Async task queues
* Multi-modal retrieval
* Autonomous planning agents
* Advanced evaluation metrics

---

# Repository Structure

```text
enterprise-agentic-rag-platform/

├── app/
│   ├── api/
│   ├── rag/
│   ├── services/
│   ├── tools/
│   ├── db/
│   ├── models/
│   └── core/
│
├── tests/
├── uploads/
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# License

MIT License

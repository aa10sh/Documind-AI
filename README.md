# 🚀 DocuMind AI

### 🧠 RAG-Based Intelligent Document Simplification & Chat System

> Upload complex documents.
> Ask contextual questions.
> Get simplified, intelligent responses powered by Retrieval-Augmented Generation (RAG).

---

## 🌟 Overview

**DocuMind AI** is a production-ready, Dockerized Retrieval-Augmented Generation (RAG) system that transforms complex documents into simplified, contextual, and intelligent conversations.

It allows users to:

* 📄 Upload PDF / DOCX documents
* 🔍 Automatically process and chunk text
* 🧠 Generate embeddings via OpenAI
* 📚 Store vectors using FAISS
* 💬 Ask contextual questions
* ✨ Receive simplified AI-generated answers

Built with a scalable **FastAPI + Docker + Nginx microservice architecture**, designed for real-world deployment.

---

## 📸 Project Screenshots

### 🏠 Application Interface
![Home]([screenshots/home.png](https://github.com/aa10sh/Documind/blob/main/Screenshot%202026-02-21%20145823.png))

### 📄 Document Upload
![Upload]([screenshots/upload.png](https://github.com/aa10sh/Documind/blob/main/Screenshot%202026-02-21%20145845.png))

### 🧠 AI Generated Summary
![Summary]([screenshots/summary.png](https://github.com/aa10sh/Documind/blob/main/Screenshot%202026-02-21%20145953.png))

### 💬 Chat with Document
![Chat]([screenshots/chat.png](https://github.com/aa10sh/Documind/blob/main/Screenshot%202026-02-21%20150251.png))

---

# 🏗️ System Architecture

User
   ↓
Frontend (Nginx)
   ↓
FastAPI Backend
   ↓
Document Processing
   ↓
Chunking Engine
   ↓
OpenAI Embeddings
   ↓
FAISS Vector Store
   ↓
RAG Response Generation
```

---

# ⚙️ Tech Stack

## 🔹 Backend

* FastAPI
* Uvicorn
* LangChain
* OpenAI API
* FAISS (Vector DB)
* Pydantic
* Loguru (Structured Logging)

## 🔹 Frontend

* HTML / CSS
* Nginx (Containerized static server)

## 🔹 DevOps & Deployment

* Docker & Docker Compose
* Docker Hub
* GitHub (CI/CD Ready)
* AWS EC2 Deployment
* Production-ready architecture

---

# 🧠 Core Features

✔ Retrieval-Augmented Generation (RAG)
✔ Vector similarity search using FAISS
✔ Context-aware document Q&A
✔ Automatic chunking & embeddings
✔ Fully Dockerized microservices
✔ Environment-based configuration
✔ Modular backend structure
✔ Production-grade deployment ready

---

# 📂 Project Structure

```
DocuMind/
│
├── backend/
│   ├── api/
│   ├── config/
│   ├── rag/
│   ├── services/
│   ├── utils/
│   └── app.py
│
├── frontend/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🐳 Docker Setup

## 1️⃣ Build Image

```bash
docker build -t documind-backend .
```

## 2️⃣ Run with Docker Compose

```bash
docker compose up --build
```

## 3️⃣ Access Application

**Frontend:**

```
http://localhost:3000
```

**Backend:**

```
http://localhost:8000
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_key_here
```

---

# 📦 Docker Hub Image

Pull production image:

```bash
docker pull aa10sh/aa10sh-documind-ai:latest
```

---

# 🔄 RAG Pipeline Flow

```
1. Document Uploaded
2. Text Extraction (PDF/DOCX)
3. Semantic Chunking
4. Embedding Generation (OpenAI)
5. Vector Storage (FAISS)
6. User Query → Embedding
7. Similarity Search
8. Context Injection into LLM
9. Intelligent Response Generated
```

---

# 🚀 Deployment Strategy

Designed for:

* GitHub Actions CI/CD
* Docker Hub Auto Push
* AWS EC2 Deployment
* Production Infrastructure

Future-ready for:

* Kubernetes
* AWS ECS / Fargate
* Vercel Frontend Integration
* Persistent Storage (S3 / DB)

---

# 📌 Roadmap

* 🔐 Multi-user authentication
* 📦 Persistent vector storage
* ⚡ Streaming responses
* 🎨 Advanced UI/UX
* 📚 Multi-document support
* 🛡 Role-based access

---

# 👨‍💻 Author

## Adarsh Singh

**Technocrat | ML & Systems Builder**

Building production-grade AI systems that bridge complexity and usability.

---

# ⭐ Why DocuMind AI?

This is not just a chatbot.
It’s a structured, scalable AI system built with:

* Engineering discipline
* Production deployment mindset
* Clean modular architecture
* Real-world DevOps practices

---





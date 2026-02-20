🚀 DocuMind AI
RAG-Based Intelligent Document Simplification & Chat System

Upload complex documents.
Ask questions.
Get simplified, intelligent responses powered by Retrieval-Augmented Generation (RAG).

🌟 Overview

DocuMind AI is a production-ready, Dockerized RAG (Retrieval-Augmented Generation) system that allows users to:

📄 Upload documents (PDF / DOCX)

🔍 Automatically process and chunk text

🧠 Generate embeddings using OpenAI

📚 Store vectors in FAISS

💬 Ask contextual questions about uploaded documents

✨ Receive simplified, intelligent responses

Built with a scalable microservice architecture using FastAPI + Docker + Nginx.

🏗️ Architecture
User
  ↓
Frontend (Nginx)
  ↓
FastAPI Backend
  ↓
Document Processing
  ↓
Chunking
  ↓
OpenAI Embeddings
  ↓
FAISS Vector Store
  ↓
RAG Response Generation
⚙️ Tech Stack
🔹 Backend

FastAPI

Uvicorn

LangChain

OpenAI API

FAISS (Vector DB)

Pydantic

Loguru (Structured Logging)

🔹 Frontend

HTML / CSS

Nginx (Containerized static server)

🔹 DevOps & Deployment

Docker & Docker Compose

Docker Hub

GitHub (CI/CD ready)

AWS EC2 (Deployment Ready Architecture)

🧠 Key Features

✔ Retrieval-Augmented Generation (RAG)
✔ Vector search using FAISS
✔ Context-aware document Q&A
✔ Automatic chunking & embedding
✔ Fully Dockerized
✔ Environment-based configuration
✔ Production-ready structure
✔ Modular backend architecture

📂 Project Structure
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
🐳 Docker Setup
1️⃣ Build Image
docker build -t documind-backend .
2️⃣ Run with Docker Compose
docker compose up --build
3️⃣ Access Application

Frontend:

http://localhost:3000

Backend:

http://localhost:8000
🔐 Environment Variables

Create a .env file:

LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_key_here
📦 Docker Hub Image

Pull the latest production image:

docker pull aa10sh/aa10sh-documind-ai:latest
🚀 Deployment Strategy

Designed for:

GitHub Actions CI/CD

Docker Hub Auto Push

AWS EC2 Deployment

Production-Grade Infrastructure

Future-ready for:

Kubernetes

ECS / Fargate

Vercel Frontend Integration

🧩 How It Works (RAG Flow)

Document uploaded

Text extracted (PDF/DOCX)

Text split into semantic chunks

Embeddings generated via OpenAI

Stored in FAISS vector database

User question converted to embedding

Relevant chunks retrieved

Context injected into LLM

Intelligent answer generated



📌 Future Improvements

Multi-user authentication

Persistent vector storage (S3 / DB)

Streaming responses

UI enhancement

Multi-document support

Role-based access

👨‍💻 Author

Adarsh Singh
Technocrat | ML & Systems Enthusiast
Building production-grade AI systems.

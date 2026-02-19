import os
from pathlib import Path

# ---------------------------------------------------
# PROJECT ROOT PATH
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DOCS_DIR = DATA_DIR / "raw_docs"
PROCESSED_DOCS_DIR = DATA_DIR / "processed_docs"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"

# Create directories if not exist
RAW_DOCS_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------
# ENV VARIABLES (Read from Windows / Docker / AWS)
# ---------------------------------------------------
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "openai")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
HF_API_KEY = os.environ.get("HF_API_KEY")

print("LLM_PROVIDER =", LLM_PROVIDER)
print("OPENAI_API_KEY loaded =", bool(OPENAI_API_KEY))

# ---------------------------------------------------
# MODEL CONFIGURATION
# ---------------------------------------------------
OPENAI_CHAT_MODEL = "gpt-4o-mini"
OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"

HF_CHAT_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
HF_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ---------------------------------------------------
# RAG CONFIGURATION
# ---------------------------------------------------
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200
TOP_K_RESULTS = 4

VECTOR_DB_TYPE = "faiss"

# ---------------------------------------------------
# APP CONFIG
# ---------------------------------------------------
APP_NAME = "DocuMind AI"
APP_VERSION = "1.0.0"
DEBUG = True

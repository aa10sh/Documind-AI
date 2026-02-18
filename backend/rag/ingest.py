from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from pathlib import Path
from typing import List

from backend.rag.embeddings import get_embedding_model
from backend.config.settings import VECTOR_STORE_DIR
from backend.config.logging import logger


# Convert chunks → LangChain Documents
def create_documents(chunks: List[str], source: str) -> List[Document]:
    documents = []

    for i, chunk in enumerate(chunks):
        doc = Document(
            page_content=chunk,
            metadata={"source": source, "chunk_id": i}
        )
        documents.append(doc)

    return documents

# Create / Update FAISS Vector Store
def ingest_documents(chunks: List[str], filename: str):
    """
    Creates or updates FAISS vector database with new document chunks.
    """

    logger.info("Starting document ingestion...")

    embeddings = get_embedding_model()
    documents = create_documents(chunks, filename)

    vector_store_path = Path(VECTOR_STORE_DIR) / "faiss_index"

    # If index already exists → load & append
    if vector_store_path.exists():
        logger.info("Loading existing FAISS index...")
        vector_store = FAISS.load_local(
            str(vector_store_path),
            embeddings,
            allow_dangerous_deserialization=True
        )
        vector_store.add_documents(documents)

    else:
        logger.info("Creating new FAISS index...")
        vector_store = FAISS.from_documents(documents, embeddings)

    # Save index
    vector_store.save_local(str(vector_store_path))

    logger.info("Document ingestion completed successfully!!")
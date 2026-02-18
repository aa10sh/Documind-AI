from langchain.vectorstores import FAISS
from pathlib import Path
from typing import List

from backend.rag.embeddings import get_embedding_model
from backend.config.settings import VECTOR_STORE_DIR, TOP_K_RESULTS
from backend.config.logging import logger

# ---------------------------------------------------
# Load FAISS Vector Store
# ---------------------------------------------------
def load_vector_store():
    vector_store_path = Path(VECTOR_STORE_DIR) / "faiss_index"

    if not vector_store_path.exists():
        raise ValueError("Vector store not found. Please upload a document first.")

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        str(vector_store_path),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


# ---------------------------------------------------
# Retrieve Relevant Chunks
# ---------------------------------------------------
def retrieve_relevant_chunks(question: str) -> List[str]:
    """
    Searches vector DB and returns top relevant chunks.
    """

    logger.info("Retrieving relevant chunks...")

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(question, k=TOP_K_RESULTS)

    chunks = [doc.page_content for doc in docs]

    logger.info(f"Retrieved {len(chunks)} relevant chunks")

    return chunks

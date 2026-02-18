from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from backend.config.settings import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    HF_API_KEY,
    OPENAI_EMBEDDING_MODEL,
    HF_EMBEDDING_MODEL
)
from backend.config.logging import logger


# Load Embedding Model (Provider Agnostic)
def get_embedding_model():
    """
    Returns embedding model based on selected provider.
    Supports OpenAI and HuggingFace.
    """

    if LLM_PROVIDER.lower() == "openai":
        logger.info("Using OpenAI Embeddings")

        return OpenAIEmbeddings(
            model=OPENAI_EMBEDDING_MODEL,
            api_key=OPENAI_API_KEY
        )

    elif LLM_PROVIDER.lower() == "huggingface":
        logger.info("Using HuggingFace Embeddings")

        return HuggingFaceEmbeddings(
            model_name=HF_EMBEDDING_MODEL
        )

    else:
        raise ValueError("Invalid LLM_PROVIDER. Choose 'openai' or 'huggingface'.")
    
    

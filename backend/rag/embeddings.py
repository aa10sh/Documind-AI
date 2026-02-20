

from langchain_openai import OpenAIEmbeddings
import os


def get_embedding_model():
    provider = os.getenv("LLM_PROVIDER", "openai")

    if provider == "openai":
        return OpenAIEmbeddings()

    else:
        raise ValueError("Only OpenAI provider is supported in this build.")
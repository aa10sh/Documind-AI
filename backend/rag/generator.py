from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate

from backend.config.settings import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    HF_API_KEY,
    OPENAI_CHAT_MODEL,
    HF_CHAT_MODEL
)
from backend.rag.prompt_templates import (
    RAG_PROMPT_TEMPLATE,
    SUMMARY_PROMPT_TEMPLATE
)
from backend.config.logging import logger

# Load LLM based on provider
def get_llm():
    if LLM_PROVIDER.lower() == "openai":
        logger.info("Using OpenAI LLM")

        return ChatOpenAI(
            model=OPENAI_CHAT_MODEL,
            api_key=OPENAI_API_KEY,
            temperature=0.3
        )

    elif LLM_PROVIDER.lower() == "huggingface":
        logger.info("Using HuggingFace LLM")

        return HuggingFaceEndpoint(
            repo_id=HF_CHAT_MODEL,
            huggingfacehub_api_token=HF_API_KEY,
            temperature=0.3,
            max_new_tokens=512
        )

    else:
        raise ValueError("Invalid LLM_PROVIDER")



# Generate Answer from Retrieved Chunks
def generate_answer(question: str, chunks: list[str]) -> str:
    """
    Generates answer using RAG pipeline.
    """

    llm = get_llm()

    context = "\n\n".join(chunks)

    prompt = PromptTemplate(
        template=RAG_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    chain = prompt | llm

    logger.info("Generating answer using LLM...")

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content



# Generate Document Summary
def generate_summary(text: str) -> str:
    """
    Generates full document summary.
    """

    llm = get_llm()

    prompt = PromptTemplate(
        template=SUMMARY_PROMPT_TEMPLATE,
        input_variables=["text"]
    )

    chain = prompt | llm

    logger.info("Generating document summary...")

    response = chain.invoke({"text": text})

    return response.content

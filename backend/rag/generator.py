from langchain_openai import ChatOpenAI
# from huggingface_hub import InferenceClient

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


# ---------------------------------------------------
# Load LLM based on provider
# ---------------------------------------------------
def get_llm():
    """
    Returns LLM client based on provider.
    OpenAI -> LangChain ChatOpenAI
    HuggingFace -> Official Router InferenceClient
    """

    if LLM_PROVIDER.lower() == "openai":
        logger.info("Using OpenAI LLM")

        return ChatOpenAI(
            model=OPENAI_CHAT_MODEL,
            api_key=OPENAI_API_KEY,
            temperature=0.3
        )

    elif LLM_PROVIDER.lower() == "huggingface":
        logger.info("Using HuggingFace LLM")

        return InferenceClient(
            model=HF_CHAT_MODEL,
            token=HF_API_KEY
        )

    else:
        raise ValueError("Invalid LLM_PROVIDER")


# ---------------------------------------------------
# Generate Answer using RAG
# ---------------------------------------------------
def generate_answer(question: str, chunks: list[str]) -> str:
    """
    RAG Pipeline:
    Question + Retrieved Chunks -> LLM -> Answer
    """

    logger.info("Generating answer using LLM...")

    context = "\n\n".join(chunks)

    prompt = RAG_PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    llm = get_llm()

    # -------- OpenAI Path --------
    if LLM_PROVIDER.lower() == "openai":
        response = llm.invoke(prompt)
        return response.content

    # -------- HuggingFace Path --------
    elif LLM_PROVIDER.lower() == "huggingface":
        response = llm.text_generation(
            prompt,
            max_new_tokens=512,
            temperature=0.3
        )
        return response


# ---------------------------------------------------
# Generate Document Summary
# ---------------------------------------------------
def generate_summary(text: str) -> str:
    """
    Full document summarization.
    """

    logger.info("Generating document summary...")

    prompt = SUMMARY_PROMPT_TEMPLATE.format(text=text)
    llm = get_llm()

    # -------- OpenAI Path --------
    if LLM_PROVIDER.lower() == "openai":
        response = llm.invoke(prompt)
        return response.content

    # -------- HuggingFace Path --------
    elif LLM_PROVIDER.lower() == "huggingface":
        response = llm.text_generation(
            prompt,
            max_new_tokens=512,
            temperature=0.3
        )
        return response

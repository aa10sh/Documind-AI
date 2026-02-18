from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

from backend.config.settings import CHUNK_SIZE, CHUNK_OVERLAP
from backend.config.logging import logger

def split_text_into_chunks(text: str) -> List[str]:
    """
    Splits large text into smaller chunks for embeddings.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""],
    )

    chunks = text_splitter.split_text(text)

    logger.info(f"Text split into {len(chunks)} chunks")

    return chunks


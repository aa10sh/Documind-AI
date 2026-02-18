from pathlib import Path
from fastapi import UploadFile
import shutil

from backend.config.settings import RAW_DOCS_DIR
from backend.config.logging import logger
from backend.utils.file_loader import load_document
from backend.utils.chunking import split_text_into_chunks
from backend.rag.ingest import ingest_documents


# Save Uploaded File
def save_uploaded_file(file: UploadFile) -> Path:
    file_path = Path(RAW_DOCS_DIR) / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"File saved: {file.filename}")

    return file_path



# Full Document Processing Pipeline
def process_document(file: UploadFile):
    """
    Full pipeline executed when user uploads a file.
    """

    logger.info("Starting document processing pipeline...")

    # 1️ Save file locally
    file_path = save_uploaded_file(file)

    # 2️ Load document text
    text = load_document(file_path)

    # 3️ Split into chunks
    chunks = split_text_into_chunks(text)

    # 4️ Store in vector database
    ingest_documents(chunks, file.filename)

    logger.info("Document processed successfully.")

    return file.filename

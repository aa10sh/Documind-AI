from pypdf import PdfReader
from docx import Document
from pathlib import Path

from backend.config.logging import logger

def load_pdf(file_path: Path) -> str:
    try:
        reader = PdfReader(str(file_path))
        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        logger.info(f"PDF loaded successfully: {file_path.name}")
        return text

    except Exception as e:
        logger.error(f"Error loading PDF: {e}")
        raise e
    

def load_docx(file_path: Path) -> str:
    try:
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

        logger.info(f"DOCX loaded successfully: {file_path.name}")
        return text

    except Exception as e:
        logger.error(f"Error loading DOCX: {e}")
        raise e

def load_txt(file_path: Path) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        logger.info(f"TXT loaded successfully: {file_path.name}")
        return text

    except Exception as e:
        logger.error(f"Error loading TXT: {e}")
        raise e


# Master Loader (Auto detect file type)
def load_document(file_path: Path) -> str:
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf(file_path)

    elif suffix == ".docx":
        return load_docx(file_path)

    elif suffix == ".txt":
        return load_txt(file_path)

    else:
        raise ValueError("Unsupported file format. Please upload PDF, DOCX, or TXT.")
import os

from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text

from app.services.vector_service import (
    create_collection,
    store_chunks
)

from app.services.metadata_service import (
    create_document,
    create_chunks
)


router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:

        content = await file.read()

        f.write(content)

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    document = create_document(
        filename=file.filename
    )

    create_chunks(
        document_id=document.id,
        chunks=chunks
    )

    create_collection()

    store_chunks(
        chunks=chunks,
        document_id=document.id,
        filename=file.filename
    )

    return {
        "document_id": document.id,
        "filename": file.filename,
        "chunks_stored": len(chunks)
    }
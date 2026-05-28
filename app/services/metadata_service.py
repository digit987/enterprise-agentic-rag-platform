from app.db.postgres import SessionLocal

from app.models.document import Document
from app.models.chunk import Chunk


def create_document(filename: str):

    db = SessionLocal()

    document = Document(
        filename=filename
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    db.close()

    return document


def create_chunks(
    document_id: int,
    chunks: list
):

    db = SessionLocal()

    chunk_objects = []

    for chunk in chunks:

        chunk_obj = Chunk(
            document_id=document_id,
            chunk_text=chunk
        )

        chunk_objects.append(chunk_obj)

    db.add_all(chunk_objects)

    db.commit()

    db.close()
from uuid import uuid4

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

from app.db.qdrant import qdrant_client
from app.services.embedding_service import embedding_model
from app.core.config import settings


def create_collection():

    existing = qdrant_client.get_collections().collections

    collection_names = [c.name for c in existing]

    if settings.COLLECTION_NAME not in collection_names:

        qdrant_client.create_collection(
            collection_name=settings.COLLECTION_NAME,

            vectors_config=VectorParams(
                size=1536,
                distance=Distance.COSINE
            ),
        )


def store_chunks(
    chunks,
    document_id,
    filename
):

    points = []

    for chunk in chunks:

        embedding = embedding_model.embed_query(chunk)

        point = PointStruct(
            id=str(uuid4()),

            vector=embedding,

            payload={
                "text": chunk,
                "document_id": document_id,
                "filename": filename
            }
        )

        points.append(point)

    qdrant_client.upsert(
        collection_name=settings.COLLECTION_NAME,
        points=points
    )
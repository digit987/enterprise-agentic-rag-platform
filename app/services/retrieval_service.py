from app.db.qdrant import qdrant_client

from app.services.embedding_service import embedding_model
from app.services.bm25_service import bm25_search
from app.services.rerank_service import rerank_chunks

from app.core.config import settings


def semantic_search(
    query: str,
    limit: int = 10
):

    query_embedding = embedding_model.embed_query(query)

    results = qdrant_client.query_points(
        collection_name=settings.COLLECTION_NAME,

        query=query_embedding,

        limit=limit
    )

    chunks = []

    for result in results.points:

        chunks.append({
            "text": result.payload["text"],
            "score": result.score,
            "filename": result.payload["filename"],
            "document_id": result.payload["document_id"]
        })

    return chunks


def hybrid_search(query: str):

    semantic_results = semantic_search(query)

    bm25_results = bm25_search(query)

    combined = semantic_results + bm25_results

    unique_chunks = {}

    for chunk in combined:

        unique_chunks[chunk["text"]] = chunk

    merged_results = list(unique_chunks.values())

    reranked = rerank_chunks(
        query=query,
        chunks=merged_results
    )

    return reranked
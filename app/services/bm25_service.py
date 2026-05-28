from rank_bm25 import BM25Okapi

from app.db.postgres import SessionLocal
from app.models.chunk import Chunk
from app.models.document import Document


def bm25_search(query: str, top_k: int = 5):

    db = SessionLocal()

    results = (
        db.query(Chunk, Document)
        .join(Document, Chunk.document_id == Document.id)
        .all()
    )

    db.close()

    documents = [
        chunk.chunk_text
        for chunk, _ in results
    ]

    tokenized_docs = [
        doc.split()
        for doc in documents
    ]

    bm25 = BM25Okapi(tokenized_docs)

    tokenized_query = query.split()

    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(
        zip(results, scores),
        key=lambda x: x[1],
        reverse=True
    )

    final_results = []

    for (chunk, document), score in ranked[:top_k]:

        final_results.append({
            "text": chunk.chunk_text,
            "score": float(score),
            "document_id": chunk.document_id,
            "filename": document.filename
        })

    return final_results
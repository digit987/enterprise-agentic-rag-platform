from sentence_transformers import CrossEncoder


reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_chunks(
    query: str,
    chunks: list,
    top_k: int = 5
):

    pairs = [
        (query, chunk["text"])
        for chunk in chunks
    ]

    scores = reranker.predict(pairs)

    reranked = []

    for chunk, score in zip(chunks, scores):

        chunk["rerank_score"] = float(score)

        reranked.append(chunk)

    reranked.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked[:top_k]
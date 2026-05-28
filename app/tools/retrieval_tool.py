from app.services.retrieval_service import (
    hybrid_search
)


def retrieval_tool(query: str):

    return hybrid_search(query)
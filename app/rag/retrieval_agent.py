from app.services.retrieval_service import hybrid_search


def retrieval_node(state):

    print("\n[Retrieval Agent]")

    retrieved_chunks = hybrid_search(
        query=state["query"]
    )

    state["retrieved_chunks"] = retrieved_chunks

    return state
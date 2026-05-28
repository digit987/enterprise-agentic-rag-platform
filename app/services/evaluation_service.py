def evaluate_response(
    response: str,
    retrieved_chunks: list
):

    context_length = sum(
        len(chunk["text"])
        for chunk in retrieved_chunks
    )

    grounded = False

    for chunk in retrieved_chunks:

        if any(
            word.lower() in chunk["text"].lower()
            for word in response.split()[:15]
        ):

            grounded = True

            break

    return {
        "grounded": grounded,
        "context_length": context_length,
        "retrieved_chunks": len(retrieved_chunks)
    }
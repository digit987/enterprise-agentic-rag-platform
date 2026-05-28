def verification_node(state):

    print("\n[Verification Agent]")

    chunks = state["retrieved_chunks"]

    verified = len(chunks) > 0

    state["verified"] = verified

    return state
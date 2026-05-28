def router_node(state):

    print("\n[Router Agent]")

    query = state["query"].lower()

    math_keywords = [
        "calculate",
        "solve",
        "+",
        "-",
        "*",
        "/"
    ]

    web_keywords = [
        "latest",
        "current",
        "news",
        "today",
        "recent"
    ]

    if any(
        keyword in query
        for keyword in math_keywords
    ):

        state["tool"] = "calculator"

    elif any(
        keyword in query
        for keyword in web_keywords
    ):

        state["tool"] = "web_search"

    else:

        state["tool"] = "retrieval"

    print(
        f"Selected tool: {state['tool']}"
    )

    return state
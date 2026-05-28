from app.tools.calculator_tool import (
    calculator_tool
)

from app.tools.retrieval_tool import (
    retrieval_tool
)

from app.tools.web_search_tool import (
    web_search_tool
)


def tool_node(state):

    print("\n[Tool Agent]")

    if state["tool"] == "calculator":

        result = calculator_tool(
            state["query"]
        )

        state["tool_result"] = result

        state["retrieved_chunks"] = []

    elif state["tool"] == "web_search":

        results = web_search_tool(
            state["query"]
        )

        state["tool_result"] = results

        state["retrieved_chunks"] = []

    else:

        retrieved_chunks = retrieval_tool(
            state["query"]
        )

        state["retrieved_chunks"] = retrieved_chunks

        state["tool_result"] = retrieved_chunks

    return state
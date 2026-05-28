from app.services.llm_service import (
    generate_rag_response
)

from app.services.memory_service import (
    save_conversation
)


def response_node(state):

    print("\n[Response Agent]")

    if state["tool"] == "calculator":

        response = (
            f"Calculation Result: "
            f"{state['tool_result']}"
        )

        state["response"] = response

        state["usage"] = {}

    elif state["tool"] == "web_search":

        web_results = state["tool_result"]

        formatted = "\n\n".join([
            f"Title: {r['title']}\n"
            f"Content: {r['content']}\n"
            f"URL: {r['url']}"
            for r in web_results
        ])

        state["response"] = formatted

        state["usage"] = {}

    else:

        llm_result = generate_rag_response(
            query=state["query"],

            context_chunks=state["retrieved_chunks"],

            history=state["history"]
        )

        state["response"] = llm_result["answer"]

        state["usage"] = llm_result["usage"]

    save_conversation(
        session_id=state["session_id"],

        user_query=state["query"],

        assistant_response=state["response"]
    )

    return state
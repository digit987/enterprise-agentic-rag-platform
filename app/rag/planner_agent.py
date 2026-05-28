from app.services.memory_service import (
    get_conversation_history
)


def planner_node(state):

    print("\n[Planner Agent]")

    history = get_conversation_history(
        session_id=state["session_id"]
    )

    state["history"] = history

    print(
        f"Loaded {len(history)} conversation turns"
    )

    return state
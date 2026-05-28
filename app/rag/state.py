from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):

    query: str

    session_id: str

    history: List

    tool: str

    tool_result: Any

    retrieved_chunks: List

    verified: bool

    response: str

    usage: Dict[str, Any]
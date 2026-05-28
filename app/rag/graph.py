from langgraph.graph import StateGraph, END

from app.rag.state import AgentState

from app.rag.planner_agent import planner_node
from app.rag.router_agent import router_node
from app.rag.tool_agent import tool_node
from app.rag.verification_agent import verification_node
from app.rag.response_agent import response_node


workflow = StateGraph(AgentState)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "router",
    router_node
)

workflow.add_node(
    "tool_executor",
    tool_node
)

workflow.add_node(
    "verification",
    verification_node
)

workflow.add_node(
    "response_generator",
    response_node
)

workflow.set_entry_point("planner")

workflow.add_edge(
    "planner",
    "router"
)

workflow.add_edge(
    "router",
    "tool_executor"
)

workflow.add_edge(
    "tool_executor",
    "verification"
)

workflow.add_edge(
    "verification",
    "response_generator"
)

workflow.add_edge(
    "response_generator",
    END
)

graph = workflow.compile()
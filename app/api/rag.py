from fastapi import APIRouter

from pydantic import BaseModel

from app.rag.graph import graph

from app.services.observability_service import RequestTimer
from app.services.evaluation_service import evaluate_response


router = APIRouter()


class QueryRequest(BaseModel):

    session_id: str

    query: str


@router.post("/chat")
async def rag_chat(request: QueryRequest):

    timer = RequestTimer()

    timer.start()

    initial_state = {

        "query": request.query,

        "session_id": request.session_id,

        "history": [],

        "retrieved_chunks": [],

        "verified": False,

        "response": "",

        "usage": {},

        "tool": "",

        "tool_result": None,
    }

    result = graph.invoke(initial_state)

    evaluation = evaluate_response(
        response=result["response"],
        retrieved_chunks=result["retrieved_chunks"]
    )

    latency = timer.stop()

    return {

        "query": request.query,

        "response": result["response"],

        "verified": result["verified"],

        "metrics": {

            "latency_seconds": latency,

            "token_usage": result["usage"],

            "evaluation": evaluation
        },

        "sources": [
            {
                "filename": chunk["filename"],
                "document_id": chunk["document_id"],
                "score": chunk.get(
                    "rerank_score",
                    chunk["score"]
                ),
                "preview": chunk["text"][:300]
            }

            for chunk in result["retrieved_chunks"]
        ]
    }
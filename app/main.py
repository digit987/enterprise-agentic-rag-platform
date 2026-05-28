from fastapi import FastAPI

from app.api.ingest import router as ingest_router
from app.api.rag import router as rag_router

from app.db.init_db import init_db


app = FastAPI(
    title="Enterprise RAG Platform",
    version="1.0.0"
)


@app.on_event("startup")
def startup():

    init_db()


app.include_router(
    ingest_router,
    prefix="/api/v1/ingest",
    tags=["Ingestion"]
)

app.include_router(
    rag_router,
    prefix="/api/v1/rag",
    tags=["RAG"]
)


@app.get("/")
async def root():

    return {
        "message": "Enterprise RAG Platform Running"
    }
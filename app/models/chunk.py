from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text
)

from app.db.postgres import Base


class Chunk(Base):

    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    chunk_text = Column(Text, nullable=False)
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.postgres import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    upload_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
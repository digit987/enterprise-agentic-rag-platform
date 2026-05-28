from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from sqlalchemy.sql import func

from app.db.postgres import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)

    session_id = Column(
        String,
        index=True
    )

    user_query = Column(Text)

    assistant_response = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
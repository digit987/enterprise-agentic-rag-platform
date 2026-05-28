from app.db.postgres import engine, Base

from app.models.document import Document
from app.models.chunk import Chunk
from app.models.conversation import Conversation


def init_db():

    Base.metadata.create_all(bind=engine)
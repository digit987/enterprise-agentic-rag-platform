from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    QDRANT_HOST = os.getenv("QDRANT_HOST")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT"))
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    COLLECTION_NAME = "documents"


settings = Settings()
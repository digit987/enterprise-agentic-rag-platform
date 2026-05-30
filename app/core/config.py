from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    COLLECTION_NAME = "documents"


settings = Settings()
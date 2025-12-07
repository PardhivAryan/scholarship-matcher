import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Scholarship Matching Platform"

    # Default: SQLite for local dev. Override with DATABASE_URL env for Postgres.
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./scholarship.db")

    JWT_SECRET: str = os.getenv("JWT_SECRET", "supersecretkey")
    JWT_ALGO: str = "HS256"

    # Redis / Elasticsearch can be used later (optional for now)
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))

    ES_HOST: str = os.getenv("ES_HOST", "http://localhost:9200")
    ES_INDEX: str = os.getenv("ES_INDEX", "scholarships-index")

settings = Settings()

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Simple Twitter"
    PROJECT_VERSION: str = "1.0.0"
    USE_SQLITE_DB: str = "True"                         # os.getenv("USE_SQLITE_DB")
    POSTGRES_USER: str = "postgres"                     # os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = "postgres"                      # os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = 5432
    POSTGRES_DB: str = "fullstack"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins


settings = Settings()
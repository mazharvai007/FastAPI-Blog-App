# core/config

import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
# env_path = Path(".") / ".env"
env_path = Path("./../.env")
load_dotenv(env_path)


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")

    POSTGRES_USER: str = os.getenv("POSTGRES_DB_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_DB_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB_NAME")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # class Config:
    #     env_file = ".env"


settings = Settings()

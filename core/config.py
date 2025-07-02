# core/config

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
# env_path = Path(".") / ".env"
# env_path = Path("./../.env")
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")

    POSTGRES_USER: str = os.getenv("POSTGRES_DB_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_DB_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB_NAME")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Rest of the code
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

    # class Config:
    #     env_file = env_path  # This tells Pydantic to load from .env


settings = Settings()

# print(f"SECRET_KEY: {settings.SECRET_KEY} ({type(settings.SECRET_KEY)})")
# print(
#     f"ACCESS_TOKEN_EXPIRE_MINUTES: {settings.ACCESS_TOKEN_EXPIRE_MINUTES} ({type(settings.ACCESS_TOKEN_EXPIRE_MINUTES)})"
# )
# print(
#     f"REFRESH_TOKEN_EXPIRE_MINUTES: {settings.REFRESH_TOKEN_EXPIRE_MINUTES} ({type(settings.REFRESH_TOKEN_EXPIRE_MINUTES)})"
# )

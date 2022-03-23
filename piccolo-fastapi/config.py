import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int
    db_url: str = Field(..., env='DATABASE_URL')

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()

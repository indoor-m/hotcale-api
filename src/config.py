from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    allow_origins: List[str] = ["https://localhost:3000"]

    class Config:
        env_file = "../.env"

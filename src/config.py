from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    allow_origins: List[str] = ["https://localhost:3000"]
    icon_url: str = ''

    class Config:
        env_file = "../.env"

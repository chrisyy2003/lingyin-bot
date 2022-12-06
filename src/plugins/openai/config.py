from pydantic import BaseSettings


class Config(BaseSettings):
    # Your Config Here
    session_token: str

    class Config:
        extra = "ignore"
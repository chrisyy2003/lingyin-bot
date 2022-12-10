from typing import List

from pydantic import BaseSettings

class Config(BaseSettings):
    # Your Config Here
    chatgpt_session_token_list : List[str] = []
    chatgpt_email_list: List[str] = []
    chatgpt_passwd_list: List[str] = []

    class Config:
        extra = "ignore"
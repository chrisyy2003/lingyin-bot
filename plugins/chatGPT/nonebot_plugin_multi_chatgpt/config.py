from typing import List

from pydantic import BaseSettings

class Config(BaseSettings):
    # Your Config Here
    chatgpt_session_token_list : List[str] = []
    chatgpt_email_list: List[str] = []
    chatgpt_passwd_list: List[str] = []
    chatgpt_proxy: str = None
    chatgpt_command_prefix: str = 'chat'
    chatgpt_cf_clearance: List[str] = []
    chatgpt_user_agent: List[str] = []

    class Config:
        extra = "ignore"
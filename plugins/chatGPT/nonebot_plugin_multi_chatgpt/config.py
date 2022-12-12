from typing import List

from pydantic import BaseSettings

class Config(BaseSettings):
    # Your Config Here
    chatgpt_session_token_list : List[str] = []
    chatgpt_email_list: List[str] = []
    chatgpt_passwd_list: List[str] = []
    chatgpt_proxy: str = None
    chatgpt_command_prefix: str = 'chat'
    chatgpt_cf_clearance: str = ''
    chatgpt_user_agent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

    class Config:
        extra = "ignore"
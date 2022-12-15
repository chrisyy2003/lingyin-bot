import asyncio
from typing import List

from pydantic import BaseSettings
from nonebot import get_driver
from .utils import yaml_load


class Config(BaseSettings):
    # Your Config Here
    chatgpt_token_path: str = "config/chatgpt_token.yml"
    chatgpt_command_prefix: str = 'chat'
    chatgpt_need_at: bool = True
    chatgpt_image_render: bool = False
    chatgpt_proxy: str = None

    class Config:
        extra = "ignore"

driver = get_driver()
global_config = driver.config
config = Config.parse_obj(global_config)

chatgpt_token_path = config.chatgpt_token_path
chatgpt_command_prefix = config.chatgpt_command_prefix
chatgpt_need_at = config.chatgpt_need_at
chatgpt_image_render = config.chatgpt_image_render
chatgpt_proxy = config.chatgpt_proxy

token_list = asyncio.run(yaml_load(chatgpt_token_path)).get('session_tokens')

config_list = [{
        "session_token": token,
        "proxy": chatgpt_proxy if chatgpt_proxy else '' ,
    } for token in token_list]

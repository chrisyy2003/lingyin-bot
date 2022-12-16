import asyncio
from pydantic import BaseSettings
from nonebot import get_driver
from nonebot.rule import to_me
import yaml


class Config(BaseSettings):
    # Your Config Here
    chatgpt_api_key_path: str = "config/chatgpt_api_key.yml"
    chatgpt_command_prefix: str = 'chat'
    chatgpt_need_at: bool = True
    chatgpt_image_render: bool = False

    class Config:
        extra = "ignore"

driver = get_driver()
global_config = driver.config
config = Config.parse_obj(global_config)

chatgpt_api_keys_path = config.chatgpt_api_key_path
chatgpt_command_prefix = config.chatgpt_command_prefix
chatgpt_need_at = config.chatgpt_need_at
chatgpt_image_render = config.chatgpt_image_render

with open(chatgpt_api_keys_path, 'r', encoding='utf-8') as f:
    api_key_list = yaml.load(f, Loader=yaml.FullLoader).get('api_keys')

from nonebot.log import logger
logger.info(f"成功加载 {len(api_key_list)}个 APIKeys")
matcher_params = {}
matcher_params['cmd'] = chatgpt_command_prefix
if chatgpt_need_at:
    matcher_params['rule'] = to_me()
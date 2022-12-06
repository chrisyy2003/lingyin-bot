from nonebot import get_driver
from .config import Config
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.log import logger
from nonebot.rule import to_me
from revChatGPT.revChatGPT import Chatbot
from nonebot import require
import time
import asyncio

scheduler = require("nonebot_plugin_apscheduler").scheduler
global_config = get_driver().config


# 配置token
config = Config.parse_obj(global_config)

chatGPT = on_command("。", aliases={"."}, priority=10, block=True)

config = {
        "Authorization": "<Your Bearer Token Here>", # This is optional
        "session_token": config.session_token
}

user_session = dict()
# 初始化bot
chatbot = Chatbot(config)

def get_chat_response(session_id, prompt):
    if session_id in user_session:
        # 如果在三分钟内再次发起对话则使用相同的会话ID
        if time.time() < user_session[session_id]['timestamp'] + 60 * 0.1:

            chatbot.conversation_id = user_session[session_id]['conversation_id']
            chatbot.parent_id = user_session[session_id]['parent_id']
    else:
        chatbot.reset_chat()
    

    try:
        resp = chatbot.get_chat_response(prompt, output="text")

        user_cache = dict()
        user_cache['timestamp'] = time.time()
        user_cache['conversation_id'] = resp['conversation_id']
        user_cache['parent_id'] = resp['parent_id']
        user_session[session_id] = user_cache

        return resp['message']
    except Exception as e:
        print(e)
        return f"发生错误: {str(e)}"

@chatGPT.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    session_id = event.get_session_id()
    msg = arg.extract_plain_text().strip()
    logger.debug(f"{session_id} {msg}")

    resp = await asyncio.get_event_loop().run_in_executor(None, get_chat_response, session_id, msg)
    await chatGPT.send(resp, at_sender = True)

# 定时刷新seesion_token
@scheduler.scheduled_job("interval", minutes=10)
async def refresh_session():
    logger.debug("refresh chatGPT session")
    chatbot.refresh_session()
scheduler.add_job(refresh_session)

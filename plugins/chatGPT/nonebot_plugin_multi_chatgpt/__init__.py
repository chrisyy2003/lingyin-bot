from .config import Config
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageEvent, GroupMessageEvent
from nonebot.params import CommandArg
from nonebot.log import logger
from revChatGPT.revChatGPT import AsyncChatbot as Chatbot, generate_uuid
from nonebot import require
import time
from .utils import user_input, output_img, yaml_load
from .config import *

scheduler = require("nonebot_plugin_apscheduler").scheduler
# 初始化chatbot

chat_bot_list: List[Chatbot] = []

@driver.on_startup
async def _():
    token_length = len(token_list)
    logger.debug(f"共加载 {token_length}个 Bot")

    fail_count = 0
    for i in config_list:
        while True:
            try:
                bot = await asyncio.get_event_loop().run_in_executor(None, Chatbot, i)
                chat_bot_list.append(bot)
                break
            except Exception as e:
                logger.error(f"bot {config_list.index(i)} 初始化失败，重试 {e}")

    if len(chat_bot_list) == 0:
        exit("chatGPT 初始化失败")
    else:
        logger.success(f"成功加载 {token_length - fail_count}个 bot")

# 用户会话ID map
user_session = dict()
# 计数
user_lock = dict()
# 使用标记
index = 0
# 标记一句话结束
punctuations = ['。', '！', '？', '.', '!', '?']


class Session:
    def __init__(self, id):
        self.session_id = id
        self.reset()

    def reset(self):
        self.conversation_id = None
        self.parent_id = generate_uuid()
        self.timestamp = 0
        self.bot_index = None

    async def get_chat_response(self, msg):
        global index
        logger.debug(f"index: {index}")
        logger.debug(f"{time.time()} {self.timestamp} {type(time.time())} {type(self.timestamp)}")
        if time.time() < self.timestamp + 60 * 10:
            bot = chat_bot_list[self.bot_index]
            bot.conversation_id = self.conversation_id
            bot.parent_id = self.parent_id
        else:
            bot = chat_bot_list[index]
            bot.reset_chat()

        index = (index + 1) % len(chat_bot_list)

        async def get_chat_text(bot: Chatbot, msg) -> dict or str:
            try:
                return await bot.get_chat_response(msg)
            except Exception as e:
                try:
                    return await bot.get_chat_response(msg)
                except Exception as e:
                    return  f"发生错误 {e}"

        resp = await get_chat_text(bot, msg)

        if isinstance(resp, dict):
            self.timestamp = time.time()
            self.bot_index = chat_bot_list.index(bot)
            self.conversation_id = resp['conversation_id']
            self.parent_id = resp['parent_id']
            return resp['message']
        else:
            self.reset()
            return resp


def get_user_session(user_id) -> Session:
    if user_id not in user_session:
        user_session[user_id] = Session(user_id)
    return user_session[user_id]

# 触发器
chatGPT = on_command(chatgpt_command_prefix, priority=10, block=True)


@chatGPT.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    session_id = event.get_session_id()
    msg = arg.extract_plain_text().strip()

    if not msg:
        return

    preprocess = user_input(msg)
    msg = preprocess[0]
    img_out_rule = preprocess[1]
    logger.debug(f"{session_id} {msg}")

    if session_id in user_lock and user_lock[session_id]:
        await chatGPT.send("消息太快啦～请稍后", at_sender=True)
    else:
        # 防止异步导致的会话parentid顺序错误
        user_lock[session_id] = True
        # resp = await session.get_chat_response(msg)
        resp = await get_user_session(session_id).get_chat_response(msg)
        resp = await output_img(resp, event, img_out_rule)
        await chatGPT.send(resp, at_sender=True)
        # 解锁
        user_lock[session_id] = False


# 定时刷新session_token
@scheduler.scheduled_job("interval", minutes=20)
async def refresh_session():
    logger.debug("refresh chatGPT session")
    for chatbot in chat_bot_list:
        # await chatbot.refresh_session()
        logger.debug(f"refresh chatGPT {chat_bot_list.index(chatbot)}")
        await asyncio.get_event_loop().run_in_executor(None, chatbot.refresh_session)
scheduler.add_job(refresh_session)

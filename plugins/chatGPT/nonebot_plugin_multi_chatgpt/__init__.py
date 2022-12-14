from nonebot import get_driver
from .config import Config
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageEvent, GroupMessageEvent
from nonebot.params import CommandArg
from nonebot.log import logger
from revChatGPT.revChatGPT import AsyncChatbot as Chatbot
from nonebot import require
import time
from nonebot.rule import to_me
import asyncio
import json
from .utils import user_input, output_img

driver = get_driver()
scheduler = require("nonebot_plugin_apscheduler").scheduler
global_config = driver.config
config = Config.parse_obj(global_config)

# 获取配置
chatgpt_token_path = config.chatgpt_token_path
chatgpt_command_prefix = config.chatgpt_command_prefix
chatgpt_need_at = config.chatgpt_need_at
chatgpt_proxy = config.chatgpt_proxy

# 获取token列表
chatgpt_session_token_list = [i for i in json.loads(open(chatgpt_token_path, 'r').read())['session_tokens']]
token_length = len(chatgpt_session_token_list)

config_list = [{
    "session_token": token,
    "proxy": chatgpt_proxy if chatgpt_proxy else ''
} for token in chatgpt_session_token_list ]

# 初始化chatbot
chat_bot_list = []
@driver.on_startup
async def _():
    logger.debug(f"共加载 {len(config_list)}个 Bot")

    global chat_bot_list

    count = 0
    for j in config_list:
        try:
            for i in config_list:
                bot = await asyncio.get_event_loop().run_in_executor(None, Chatbot, i)
                logger.debug(f"bot {config_list.index(i) + 1} 初始化成功")
                chat_bot_list.append(bot)
                count += 1
        except Exception as e:
            logger.error(f"bot初始化失败+1")
            pass
    if len(chat_bot_list) == 0:
        exit("chatGPT 初始化失败")
    else:
        logger.success(f"成功加载 {count}个 bot")

# 用户会话ID map
user_session = dict()
# 计数
user_lock = dict()
# 使用标记
index = 0
# 标记一句话结束
punctuations = ['。', '！', '？', '.', '!', '?']


def use_old_chatbot(session_id) -> bool:
    logger.info(
        f"{session_id in user_session} {session_id in user_session and time.time() < user_session[session_id]['timestamp'] + 60 * 20}")
    if session_id in user_session:
        # 如果在20分钟内再次发起对话则使用相同的会话ID
        if time.time() < user_session[session_id]['timestamp'] + 60 * 20:
            logger.debug("使用之前的")
            return True
    return False


async def get_chat_response(session_id, prompt):
    global index
    logger.debug(f"index: {index}")

    if use_old_chatbot(session_id):
        chatbot = chat_bot_list[user_session[session_id]['bot_index']]
        chatbot.conversation_id = user_session[session_id]['conversation_id']
        chatbot.parent_id = user_session[session_id]['parent_id']
    else:
        # 超时或者如果没有发起过对话则获取新的chatbot
        chatbot = chat_bot_list[index]
        chatbot.reset_chat()

    msg = ''
    try:
        user_cache = dict()
        if not use_old_chatbot(session_id):
            logger.info("新用户")
            user_cache['bot_index'] = index
        else:
            user_cache['bot_index'] = user_session[session_id]['bot_index']
            logger.info("老用户")

        index = (index + 1) % token_length

        resp = await chatbot.get_chat_response(prompt)

        user_cache['timestamp'] = time.time()
        user_cache['conversation_id'] = resp['conversation_id']
        user_cache['parent_id'] = resp['parent_id']
        user_session[session_id] = user_cache

        return resp['message']

        # TODO: 是否需要增加长消息的功能
        # while True:
        #     if msg == '':
        #         resp = chatbot.get_chat_response(prompt)
        #     else:
        #         # 不是第一次请求
        #         resp = chatbot.get_chat_response("继续")
        #     msg += resp['message']
        #     # 如果最后一个字符是结尾标点符号则退出
        #     if resp['message'][-1] in punctuations:
        #         handle_cache(resp, session_id)
        #         return msg
    except Exception as e:
        try:
            user_cache = dict()
            user_cache['bot_index'] = index
            index = (index + 1) % token_length
            chatbot.reset_chat()
            resp = await chatbot.get_chat_response(prompt)
            user_cache['timestamp'] = time.time()
            user_cache['conversation_id'] = resp['conversation_id']
            user_cache['parent_id'] = resp['parent_id']
            user_session[session_id] = user_cache

            return resp['message']

        except Exception as e:
            logger.error(e)
            user_lock[session_id] = False
            return f"发生错误 {str(e)}"


# 触发器
chatGPT = on_command(chatgpt_command_prefix, priority=10, block=True)
@chatGPT.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    session_id = event.get_session_id()
    msg = arg.extract_plain_text().strip()

    if not msg:
        return
    img_out_rule = False
    preprocess = user_input(msg)
    msg = preprocess[0]
    img_out_rule = preprocess[1]
    logger.debug(f"{session_id} {msg}")
    # logger.info(user_session)

    if session_id in user_lock and user_lock[session_id]:
        await chatGPT.send("消息太快啦～请稍后", at_sender=True)
    else:
        # 防止异步导致的会话parentid顺序错误，所以需要上锁
        user_lock[session_id] = True
        resp = await get_chat_response(session_id, msg)
        resp = await output_img(resp, img_out_rule)
        await chatGPT.send(resp, at_sender=True)
        # 解锁
        user_lock[session_id] = False

# 定时刷新seesion_token
@scheduler.scheduled_job("interval", minutes=20)
async def refresh_session():
    logger.debug("refresh chatGPT session")
    for chatbot in chat_bot_list:
        # await chatbot.refresh_session()
        logger.debug(f"refresh chatGPT {chat_bot_list.index(chatbot)}")
        await asyncio.get_event_loop().run_in_executor(None, chatbot.refresh_session)
scheduler.add_job(refresh_session)

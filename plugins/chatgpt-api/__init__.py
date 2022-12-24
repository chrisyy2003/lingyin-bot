import time
import aiohttp
import requests

from nonebot.log import logger
from nonebot_plugin_htmlrender import md_to_pic

chat_bot_list = []

index = 0

chat_bot_list = requests.get('http://127.0.0.1:3000/len').json()['len']


class Session:
    def __init__(self, id):
        self.session_id = id
        self.reset()

    def reset(self):
        self.conversation_id = None
        self.parent_id = None
        self.bot_index = None
        self.timestamp = 0

    async def get_chat_response(self, msg):
        global index

        if time.time() < self.timestamp + 60 * 10:
            bot = self.bot_index
        else:
            bot = index
            self.reset()

        index = (index + 1) % chat_bot_list

        async def chat(bot_id, msg, c_id=None, p_id=None) -> dict or str:
            if c_id:
                params = {
                    'msg': msg,
                    'bot_id': bot_id,
                    'conversationId': c_id,
                    'messageId': p_id
                }
            else:
                params = {
                    'msg': msg,
                    'bot_id': bot_id
                }

            logger.debug(params)
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get('http://127.0.0.1:3000/chat', params=params) as resp:
                        r = await resp.json()
                        return r
                except Exception as e:
                    try:
                        async with session.get('http://127.0.0.1:3000/chat', params=params) as resp2:
                            r = await resp2.json()
                            return r
                    except Exception as e:
                        return f"发生错误 {e}"
                    return f"发生错误 {e}"

        resp = await chat(bot, msg, self.conversation_id, self.parent_id)

        if isinstance(resp, dict):
            self.timestamp = time.time()
            self.bot_index = bot
            self.conversation_id = resp['conversationId']
            self.parent_id = resp['messageId']
            return resp['response']
        else:
            self.reset()
            return resp


user_session = {}


def get_user_session(user_id) -> Session:
    if user_id not in user_session:
        user_session[user_id] = Session(user_id)
    return user_session[user_id]


user_lock = {}

from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment, PrivateMessageEvent


reset_c = on_command("重置", priority=9, block=True)
@reset_c.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    session_id = event.get_session_id()
    msg = arg.extract_plain_text().strip()
    get_user_session(session_id).reset()
    await reset_c.finish("会话已重置")

chatgpt = on_command('。', priority=9, block=True)


@chatgpt.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    session_id = event.get_session_id()
    msg = arg.extract_plain_text().strip()

    if not msg:
        return

    if session_id in user_lock and user_lock[session_id]:
        await chatgpt.send("消息太快啦～请稍后", at_sender=True)
    else:
        user_lock[session_id] = True
        resp = await get_user_session(session_id).get_chat_response(msg)

        if len(resp) > 120:
            if resp.count("```") % 2 != 0:
                resp += "\n```"
            img = await md_to_pic(resp)
            resp = MessageSegment.image(img)
        await chatgpt.send(resp, at_sender=True)

        user_lock[session_id] = False

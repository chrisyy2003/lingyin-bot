from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Message, MessageEvent, GroupMessageEvent, MessageSegment

from nonebot.params import CommandArg
from nonebot.plugin import on_command

echo = on_command("echo", to_me())

@echo.handle()
async def handle_echo(event: MessageEvent, message: Message = CommandArg()):
    print(event.message_id)
    await echo.send(MessageSegment.reply(event.message_id) + "good")

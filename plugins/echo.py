from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import Message, MessageEvent, PrivateMessageEvent, MessageSegment


weather = on_command('test', priority=5)
@weather.handle()
async def handle_first_receive(matcher: Matcher, event: MessageEvent, args: Message = CommandArg()):
    await matcher.finish(event.get_session_id())
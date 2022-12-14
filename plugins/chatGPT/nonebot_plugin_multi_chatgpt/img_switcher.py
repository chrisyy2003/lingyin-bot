# python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 1:54
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : img_switcher.py
# @Software: PyCharm
import yaml

from .path import *
from .utils import *
from nonebot import logger

from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import (
    MessageSegment,
    MessageEvent,
    GroupMessageEvent,
    PrivateMessageEvent,
    Message, Bot)
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11.permission import GROUP_ADMIN, GROUP_OWNER
from nonebot_plugin_htmlrender import md_to_pic, text_to_pic

global_out = on_command("全局图片", aliases={"gpt全局图片"}, priority=1, block=True, permission=SUPERUSER)


@global_out.handle()
async def _(arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    config_history = await yaml_load(IMG_OUT_CONFIG)
    if '开' in msg:
        if config_history.get('global'):
            await global_out.finish('已是开启状态')
        await yaml_upload(IMG_OUT_CONFIG, {'global': True})
        await global_out.finish('已开启全局图片输出')
    elif '关' in msg:
        if not config_history.get('global'):
            await global_out.finish('已是关闭状态')
        await yaml_upload(IMG_OUT_CONFIG, {'global': False})
        await global_out.finish('已关闭全局图片输出')
    else:
        pass


group_out = on_command("群图片", aliases={"gpt群图片"}, priority=1, block=True,
                       permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER)


@group_out.handle()
async def _(event: GroupMessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    config_history = await yaml_load(IMG_OUT_CONFIG)
    if '开' in msg:
        if event.group_id in config_history.get('groups'):
            await group_out.finish('已是开启状态')
        config_history.get('groups').append(event.group_id)
        await yaml_upload(IMG_OUT_CONFIG, {'groups': config_history.get('groups')})
        await group_out.finish('已开启本群图片输出')
    elif '关' in msg:
        if event.group_id not in config_history.get('groups'):
            await group_out.finish('已是关闭状态')
        config_history.get('groups').remove(event.group_id)
        await yaml_upload(IMG_OUT_CONFIG, {'groups': config_history.get('groups')})
        await group_out.finish('已关闭本群图片输出')
    else:
        pass


user_out = on_command("对我输出图片", aliases={"对我输出"}, priority=1, block=True)


@user_out.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    uid = event.user_id
    config_history = await yaml_load(IMG_OUT_CONFIG)
    at = ""
    if isinstance(event, GroupMessageEvent):
        at = MessageSegment.at(uid)
    if '开' in msg:
        if uid in config_history.get('users'):
            await user_out.finish(at + '已是开启状态')
        config_history.get('users').append(uid)
        await yaml_upload(IMG_OUT_CONFIG, {'users': config_history.get('users')})
        await user_out.finish(at + '已开启对你输出图片')
    elif '关' in msg:
        if uid not in config_history.get('users'):
            await user_out.finish(at + '已是关闭状态')
        config_history.get('users').remove(uid)
        await yaml_upload(IMG_OUT_CONFIG, {'users': config_history.get('users')})
        await user_out.finish(at + '已关闭对你输出图片')
    else:
        pass


check_switch_list = on_command("查看输出", aliases={"查看图片输出", "查看图片开关"}, priority=1, block=True,
                               permission=SUPERUSER)


@check_switch_list.handle()
async def _(bot: Bot, event: MessageEvent):
    config_history = await yaml_load(IMG_OUT_CONFIG)
    msg = ""
    msg += f"全局图片输出：\n - {'开启' if config_history.get('global') else '关闭'}\n"
    msg += f"\n群图片输出：\n "
    for group in config_history.get('groups'):
        g_name = (await bot.get_group_info(group_id=group))["group_name"]
        msg += f" - {g_name}：{group}\n"
    msg += f"\n用户输出：\n "
    for user in config_history.get('users'):
        u_name = (await bot.get_stranger_info(user_id=user))["nickname"]
        msg += f" - {u_name}:{user}\n"
    img = await text_to_pic(msg)
    await check_switch_list.finish(MessageSegment.image(img))


config_handler = on_command("图片输出删除", aliases={"输出删除"}, priority=1, block=True, permission=SUPERUSER)


@config_handler.handle()
async def _(event: MessageEvent, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    if not msg:
        return
    mode = "g"
    if "u" in msg:
        mode = "u"
        msg = msg.replace("u", "")
    msgs = msg.split()
    r = ""
    if msgs:
        for id_ in msgs:
            if id_.isdigit():
                history_config = await yaml_load(IMG_OUT_CONFIG)
                if mode == "g":
                    if id_ in history_config.get('groups'):
                        history_config.get('groups').remove(id_)
                        await yaml_upload(IMG_OUT_CONFIG, {'groups': history_config.get('groups')})
                        r += f"已删除群：{id_}\n"
                    else:
                        r += f"群：{id_}不存在\n"
                elif mode == "u":
                    if id_ in history_config.get('users'):
                        history_config.get('users').remove(id_)
                        await yaml_upload(IMG_OUT_CONFIG, {'users': history_config.get('users')})
                        r += f"已删除用户：{id_}\n"
                    else:
                        r += f"用户：{id_}不存在\n"
            else:
                r += f"无效的id：{id_}\n"
        await config_handler.finish(r)
    else:
        pass



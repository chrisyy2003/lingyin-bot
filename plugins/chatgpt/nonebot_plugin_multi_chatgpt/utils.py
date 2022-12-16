# python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 0:58
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : utils.py
# @Software: PyCharm
from typing import Union, Tuple

from nonebot.adapters.onebot.v11 import Event, MessageSegment, MessageEvent, GroupMessageEvent, PrivateMessageEvent
from nonebot_plugin_htmlrender import md_to_pic
from .path import *


def user_input(msg: str) -> Tuple[str, bool]:
    """
    消息预处理
    :param msg: 纯文本消息
    :return: （msg, bool）
    """
    if msg.startswith('-p'):
        msg = msg.replace('-p', '', 1)
        return msg, True
    elif msg.endswith('-p'):
        msg = msg.replace('-p', '', 1)
        return msg, True
    return msg, False


async def output_img(resp: str, event: MessageEvent, img_out_rule: bool) -> Union[MessageSegment, str]:
    if resp.count("```") % 2 != 0:
        resp += "\n```"
    if img_out_rule:
        img = await md_to_pic(resp)
        return MessageSegment.image(img)

    img_out_config = await yaml_load(IMG_OUT_CONFIG)
    if img_out_config.get('global'):
        img = await md_to_pic(resp)
        return MessageSegment.image(img)
    if isinstance(event, GroupMessageEvent):
        if event.group_id in img_out_config.get('groups'):
            img = await md_to_pic(resp)
            return MessageSegment.image(img)
        else:
            if event.user_id in img_out_config.get('users'):
                img = await md_to_pic(resp)
                return MessageSegment.image(img)
    if isinstance(event, PrivateMessageEvent):
        if event.user_id in img_out_config.get('users'):
            img = await md_to_pic(resp)
            return MessageSegment.image(img)
    return resp


async def yaml_load(path: Union[Path, str]) -> dict:
    """
    读取yaml文件
    :param path: 文件路径
    :return:
    """
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


async def yaml_dump(path: Union[Path, str], data: dict) -> None:
    """
    写入yaml文件
    :param path: 文件路径
    :param data: 数据
    :return:
    """
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
        f.close()


async def yaml_upload(path: Union[Path, str], data: dict) -> None:
    """
    更新yaml文件
    :param path: 文件路径
    :param data: 数据
    :return:
    """
    raw = await yaml_load(path)
    raw.update(data)
    await yaml_dump(path, raw)

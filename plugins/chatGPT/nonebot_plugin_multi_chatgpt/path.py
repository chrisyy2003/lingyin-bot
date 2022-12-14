# python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 0:59
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : path.py
# @Software: PyCharm
from pathlib import Path

import yaml
from nonebot import get_driver

LOCAL = Path() / "config_multi_chatgpt"
IMG_OUT_CONFIG = LOCAL / "img_out_config.yml"


@get_driver().on_bot_connect
async def _():
    LOCAL.mkdir(exist_ok=True)
    if not IMG_OUT_CONFIG.exists():
        with open(IMG_OUT_CONFIG, 'w', encoding='utf-8') as f:
            config = {"global": False, "groups": [], "users": []}
            yaml.dump(config, f, allow_unicode=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from nonebot.log import logger, logger_id, default_filter
import sys

# 删除默认日志
logger.remove(logger_id)
# 日志格式
default_format: str = (
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level:<7}</lvl>] "
    "<c><u>{name}</u></c> | "
    "{message}"
)
# 控制台
logger.add(sys.stdout, level=0, diagnose=False, filter=default_filter, format=default_format)
# 文件日志
logger.add("log/bot.log", rotation="00:00", diagnose=False, level="DEBUG", format=default_format)

nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

# 请不要修改这个文件，除非你知道你在做什么！
nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app")

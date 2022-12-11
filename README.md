# Lingyin Bot

## 启动机器人

1.  `pip3 install poetry` 安装peorty包管理器和onebot适配器
2.  `poetry install` 安装依赖
3.  `poetry run python3 bot.py` 启动bot
<!-- 3.  `source venv/bin/activate && python3 bot.py` 启动bot -->

# 作为插件安装

Lingyin Bot中的源码已作为插件发布，如果觉得有帮助需要继承到自己的Bot中可以使用两种方法：

1.  直接复制源码中的插件到自己的bot的plugin目录下，然后加上相应的配置即可
2.  通过包管理器安装，可以通过nb，pip3，或者poetry等方式安装

第一种可能需要一定的基础，第二种几行命令就可以搞定，但是方便自定义功能。
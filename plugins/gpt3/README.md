<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# Nnonebot-plugin-gpt3

_✨ 基于openai GPT3官方API的对话插件 ✨_

<p align="center">
  <img src="https://img.shields.io/github/license/EtherLeaF/nonebot-plugin-colab-novelai" alt="license">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/nonebot-2.0.0r4+-red.svg" alt="NoneBot">
  <a href="https://pypi.python.org/pypi/nonebot-plugin-gpt3">
      <img src="https://img.shields.io/pypi/dm/nonebot-plugin-gpt3" alt="pypi download">
  </a>
</p>


</div>

## 功能

- [x] 上下文
- [x] 会话导出
- [x] 返回文字图片渲染
- [x] 每个人单独会话
- [ ] 更多配置

## 安装

1.  使用 nb-cli

```
nb plugin install nonebot_plugin_gpt3
```

2.   通过包管理器安装，可以通过nb，pip3，或者poetry等方式安装，以pip为例

```
pip install nonebot_plugin_gpt3
```

随后在`bot.py`中加上如下代码，加载插件

```
nonebot.load_plugin('nonebot_plugin_gpt3')
```

## 配置

对于官方openai接口只需配置API Keys即可，所以请填写API在您配置的`chatgpt_token_path`下面，默认路径是`config/chatgpt_img_config.yml`

文件内格式如下，有多个Key请按照如下格式配置。

```
api_keys:
  - XXX
  - YYY
```

之后是一些自定义配置，根据注释可以自行修改，如果需要配置请在`env.dev`下进行配置。

```
chatgpt_api_key_path = "config/chatgpt_api.yml" # api文件
chatgpt_command_prefix = "chat"									# 触发聊天的前缀
chatgpt_need_at = False													# 是否需要@
chatgpt_image_render = False										# 是否需要图片渲染
```


## 如何使用？


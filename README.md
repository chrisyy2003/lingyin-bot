# Lingyin Bot

## 启动机器人

1.  `pip3 install poetry` 安装peorty包管理器和onebot适配器
2.  `poetry install` 安装依赖
3.  `source .venv/bin/activate && python3 bot.py` 启动bot

# 作为插件安装

Lingyin Bot中的源码已作为插件发布，如果觉得有帮助需要继承到自己的Bot中可以使用两种方法：

1.  直接复制源码中的插件到自己的bot的plugin目录下，然后加上相应的配置即可
2.  通过包管理器安装，可以通过nb，pip3，或者poetry等方式安装

第一种可能需要一定的基础，第二种几行命令就可以搞定，但是方便自定义功能。

## 多账户ChatGPT

### 安装

~~第一种方式~~（暂时不行，等待pr通过）

```
nb plugin install nonebot_plugin_multi_chatgpt
```

------

第二种方式，使用一下命令安装

```
pip3 install nonebot-plugin-multi-chatgpt==1.0.0
```

随后在`bot.py`中加上如下代码，加载插件

```
nonebot.load_plugin('nonebot_plugin_multi_chatgpt')
```

### 配置

在`.env.dev`中配置自己的`chatgpt_session_token_list`即可

具体方法如下：

1. 随后在转到https://chat.openai.com/chat并登录或注册
2. 按F12打开Chrome控制台
   ![image-20221206173841156](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221206173841156.png)
3. 打开Application选项卡 > Cookie
   ![](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221205094326498.png)
4. 复制值`__Secure-next-auth.session-token`并将其粘贴到在`.env.dev`中`session_token`即可。不需要管Authorization的值。

### Todo

- [ ] 返回值渲染为图片
- [ ] 完善密码登陆

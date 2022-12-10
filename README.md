# Lingyin Bot

## 启动机器人

1.  `pipi3 install peotry nonebot-adapter-onebot ` 安装peorty包管理器和onebot适配器
2.  `peotry install ` 安装依赖
3.  `peotry run nb run` 启动bot

## ChatGPT插件

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

## Todo

- [ ] 返回值渲染为图片

# Lingyin Bot

## How to start

1. `pip3 install -r requirements.txt`安装requirements.txt中的依赖
2. `python3 bot.py`启动Bot

## ChatGPT

在`.env.dev`中配置自己的`session_token`即可

具体方法如下：

1. 随后在转到https://chat.openai.com/chat并登录或注册
2. 按F12打开Chrome控制台
   ![image-20221206173841156](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221206173841156.png)
3. 打开Application选项卡 > Cookie
   ![](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221205094326498.png)
4. 复制值`__Secure-next-auth.session-token`并将其粘贴到在`.env.dev`中`session_token`即可。不需要管Authorization的值。

## Todo

- [ ] 返回值渲染为图片

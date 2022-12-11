## 多账户ChatGPT

### 安装

~~第一种方式~~（暂时不行，等待pr通过）

```
nb plugin install nonebot_plugin_multi_chatgpt
```

------

第二种方式，使用一下命令安装

```
pip3 install nonebot_plugin_multi_chatgpt --upgrade
```

随后在`bot.py`中加上如下代码，加载插件

```
nonebot.load_plugin('nonebot_plugin_multi_chatgpt')
```

### 配置

在`.env.dev`中配置自己的`chatgpt_session_token_list`即可

多个token，请注意不能换行只能写成一排 例如 

```
chatgpt_session_token_list = ["xxx", "yyy", "zzz"]
```

如果只有一个session也需要用数组的形式 

```
chatgpt_session_token_list = ["xxxx"]
```

获取token得方法，打开Application选项卡 > Cookie，复制值`__Secure-next-auth.session-token`并将其粘贴到在`.env.dev`中`session_token`即可。不需要管Authorization的值。
![](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221205094326498.png)

### Todo

- [ ] 返回值渲染为图片
- [ ] 完善密码登陆

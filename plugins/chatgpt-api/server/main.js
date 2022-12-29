import express from 'express';
import { ChatGPTAPIBrowser } from 'chatgpt'


var app = express();

const config = [
    {
        email: 'osyyjozylg@iubridge.com',
        password: 'yy123123'
    },
    {
        email: 'lgfo353p@linshiyouxiang.net',
        password: 'yy123123'
    }
]


let bot_list = []

async function init_bot() {
    console.log(config)
    for (let i = 0; i < config.length; i++) {
        const api = new ChatGPTAPIBrowser(config[i])
        try {
            await api.initSession()
            bot_list.push(api)
        }catch (e) {
            console.log(config[i].email, 'fail...')
        }
    }
}

app.use((req, res, next) => {
    const now = new Date(Date.now())
    console.log(now.toLocaleDateString() ,now.toLocaleTimeString(), req.url)
    next()
})


app.get('/chat', async (req, res) => {
    const msg = req.query.msg
    const bot_id = req.query.bot_id
    const conversationId = req.query.conversationId
    const messageId = req.query.messageId

    console.log(conversationId, messageId);
    let result
    try{
        if (conversationId == undefined) {
            result = await bot_list[bot_id % bot_list.length].sendMessage(msg)
            res.send(result);
            return
        }else {
            result = await bot_list[bot_id % bot_list.length].sendMessage(msg, {
                conversationId: conversationId,
                parentMessageId: messageId
            })
            res.send(result);
            return
        }
    }catch (e) {
        return e
    }
});

app.get('/len', function (req, res) {
    res.send({
        len: config.length
    });
});

app.get('/bot', function (req, res) {
    res.send({
        bot: bot_list
    });
});

app.get('/re', async (req, res) => {
    const id = req.query.id
    await bot_list[id % config.length].refreshSession()
    res.send('ok');
});


init_bot().then(() => {
    app.listen(3000, () => {
        console.log('express start...')
    })
})

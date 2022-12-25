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

  for (let i = 0; i < config.length; i++) {
        const api = new ChatGPTAPIBrowser(config[i])
        try {
            await api.initSession()
            bot_list.push(api)
        }catch (e) {
            console.log(e)
        }
    }
}


app.get('/chat', async (req, res) => {
    const msg = req.query.msg
    const bot_id = req.query.bot_id
    const conversationId = req.query.conversationId
    const messageId = req.query.messageId

    

    console.log(conversationId, messageId);
    let result
    if (conversationId == undefined) {
        result = await bot_list[bot_id].sendMessage(msg)
    }else {
        result = await bot_list[bot_id].sendMessage(msg, {
            conversationId: conversationId,
            parentMessageId: messageId
        })

    }
    console.log(result)
    res.send(result);
});

app.get('/len', function (req, res) {
    res.send({
        len: config.length
    });
});


init_bot().then(() => {
    app.listen(3000, () => {
        console.log('express start...');
    })
})

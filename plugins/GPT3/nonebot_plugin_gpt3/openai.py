import asyncio
from typing import Awaitable

import openai

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def get_chat_response(msg) -> str:
    openai.api_key = "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"
    try:
        response : str = openai.Completion.create(
            model="text-davinci-003",
            prompt=msg,
            temperature=0.9,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        res = response['choices'][0]['text'].strip()
        if start_sequence[1:] in res:
            res = res.split(start_sequence[1:])[1]
        return res, True
    except Exception as e:
        return f"发生错误: {e}", False

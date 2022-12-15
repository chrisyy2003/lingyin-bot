import asyncio

from revChatGPT.revChatGPT import AsyncChatbot as Chatbot, generate_uuid
token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..LqHxi_dkRNScB9up.U53Nwmv2Fx1e4ImGl-tTZx2pl_XMqj-vhesOK1TlcYb-1psy9zjXEdCo-ymLz5Y0YvV2zrho6v19R-ucjCpWn7kqssZjZkoPXYmm3fR7YXG3gXqEzmliX7DjLXIdhfbZ91XXS9WxeD0mKb1kaNaGUJWxUKs3VFRIH5PxVcp9P6nTJ3-tQ4iYQTF_JFkesBVEc8aejTxmgcvLY6UKub4sXt5EMfkxKXbL--MQAnW7ct8c3Eb-joGofLQLC-L48AGqDr5GqB_UQcswcjtQ_m9jPlIzBDyowSoi4o2wFQqu8pO4Y7ZFBbFsXPnVSjOONn99QeSuOghAyNHEp5sOaQ_-5C6FDOrIA8LjQCT1LHpbZNDeg42FWCdJRmj1jWFwOw6tZ-5tgyDpoYD8l2OEyI1-DEQ1snQItwFpnUqUy1V6mN9PXp-6KT4va5Es8ldjmaVeAv0W7bp-Orv03BVjd5FeOKNSKQi7v6Hcgy7BBKxwzBM9VerZyxlHqkPlSp_p9jf7s80aYGhIBwZ8t1ZxI3YBeWFortnJRGDAwV2m0HlNo63V05NeG5GIRl8pV0EKac8QaxajNyiOMMu-3Kd_79hnH87ncj3oenxfX_z0RLCriCO8qQMr_3D6pm4eK5p4yfthnCIZcRm3LJdfC3VZeKcUKkPHrTWCk4xpkfqAUpOi3xtezCWO188AURxShLzxOYoCBu9cBPEY32g67UAcMP6ioJc8P-PKxm4R1huIqno9IVsIFpc6fwokdP3AG-IJtxq7Lv6oCXmef6fF0QR6LwVuqdSHWe9vELT-wIjyDu6_8p8cuPRH1B9RKvhPJ_ajrURLk-cJTrDWtqEaZQFOhDWfJrpxwW71VyxXNwW0kI5_aHshZJRlUeZWK4y1JBg_bbfBtUlD4wz5qUf5fhJFwauVHMNSeQHXltP5vBfir74hOTvv_fdY9xDS2DUhYgPtY_Q0hnkrQM4bYlV6EnB1ggamdiHn9WofpnB0wYJBXQsDZEGFV4SdTbMTGlhBv1Cb7d2l4ldZSeu5DyB43YY1jeKHiV0KZK7klOycMsVIqcoSzV4XV-YZjFopm6x11Wbb3BVunWxNmXJZ0glcCFhT33FzVBTjQMzYpgCJGb6Rk0cPRpjSMbuMN3uyzX7P_rC5ekz9GXWGzBSle09aSezyqNGL2gUV1xS9e-zv1kWFn7ZKdNqZU0cgq1Z2Bn6i4WBCdkFxk-g1_8tTP4jmTakd10Bs23PDiLnDzrOCdf0Ims8omKnUhNrrZY2Frd9gLtl41RN115C_bGIinaIe17-DG3W3GVoBZ9WoUI9nkoWP1Bbe8SnGxe6CJnflJ54oV8-j05vOvdhLmCoMzSZj5tlHba5TvRicWWKEg-QkcHGqCsJY_rvuQZtKrHm25jIdm1aXpRyOU-m1Ccllkuyl-jQloSi_Eqo_YAlT8eZGxP1LXeAbMfretCJPWSkwSnuIgNG9jt8LMNW_oQ-0E9NWyR3Z7hIfsPYRiS3MIkQ_UxVzyhJDuoYF0oeDm70amnCnZLU4Fik7k3jwBhixGFAUjKpsLb2CWuWcIp00PPpsQ1wSdy9FXQyMpRNrrJ48v2cxkErQr1syFECx7G30KPPe34FKK-PwSp8XmWU1o_C2dBWDMsmqpXizqkjCGyUutf16CeMHtLKEQj91Mh9q5CoPNSaMgla2Y7o4NA1Z1DmJSEnECqmsx84wRY7954cZh_ge3u5qYTxUyl4f-EUwWw8D3ZTzkQkfQ2IQSv5aicFTi8JACSL4PnveHMdl7emLUwgaFJaEkme78eWtLYA5A05MvFLMb-Im9dTn7qi6DiVT7SKd_Zu6zyF5jQG2_7K_lb4aIuTCqNxZtBubtkRvNBgp31Q3HCFkNNA60bn4zFeaMrXsBNoMbpT_kjrGLNA4M6JavH6CUpInuer50QE6JZJ0X9G-dBKnR0MnFrEtkY07nlQz_aNp6GgCNYZO8A2Lg19gUGtsyMEW1uWkq3ALzdXz3cx9ywEQWhWuqknSFAeS4YK8nDZSO9N2TG_OnYyaMrp2N_V0zfytq2Bnnk6MiBEMbto_OHr4UJv3bmO3GUPuWmDoszbJS1kB3upPs6P93HS2-Vua4CotoZPVS9_rEkqNX9_s070s70JRbIdl33ce0Mk2qN7M3pB5aaBLJ2G8BlX1vJnpQYCYdlCdxZ2BijRCtkiDB7gKQ1T2X_8FIxt8VeDX4mPPk522dEEf2KlkWrSlM7VtcNAdr1cheQTe4ooFUg.lR1plMeexqNCdm6oyLCoOA"

config = {
    "session_token": token
}

async def main():
    bot = await asyncio.get_event_loop().run_in_executor(None, Chatbot, config)
    res = await bot.get_chat_response("hello")
    print(res)
    #
    # while msg := input("输入问题: "):
    #     res = await chatbot.get_chat_response(msg)
    #     print(res)


loop = asyncio.get_event_loop() # 创建事件循环
loop.run_until_complete(main())
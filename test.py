from revChatGPT.revChatGPT import Chatbot

# a =  {':authority': 'chat.openai.com', ':method': 'GET', ':path': '/backend-api/models', ':scheme': 'https', 'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9', 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJva3BjenU2MjcxMEBjaGFjdW8ubmV0IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJKUCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZm5BVVlrUDVPNEN0ZWJVY2pGSFp0N1F3In0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzkyZDA0MmU1NjQ4MTFjNTU2NzBiMTIiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzA5MjAyMTUsImV4cCI6MTY3MDk2MzQxNSwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvZmZsaW5lX2FjY2VzcyJ9.JGQR9MgjOEovLBT-16ubFQth8al8S-IVmqaIVa-2Awwty8ERSiTaroiEa2o1l1nGvCGgqDWayf31lcNTTh91qJUrCVMy-QgBdJGRc1EY0gjgmoA3Fp4L1OMM5WQVfAt6QjvVr1Zudf1Udpm4ASNNd8XjJI5qOw9lQNap6XWrU8nRNyqdgBiBG4LeSGXbNBwEgTDWaN3qO9uJ84h2bzGjW9vNy38yVeSYaNJUGkmE5laOZHC4WPBMafYYnbNMxSaiwfSY38N2JLISRd7JxdL0rcyVP_jhsRBvUl2mGNCSAgZ8-IA3VtwXsC3JFHxwV76NQ2n7WcsaBZzFxCon-uXoRQ', 'content-type': 'application/json', 'cookie': 'cf_clearance=qAqpd46ZtjCLU2769vdOf5hMD9pQWgJanRJQxCaki9g-1670920174-0-1-9eceed06.2c14db7a.c9cfb2e6-160; __Host-next-auth.csrf-token=67b5f88afad43795c78f38a5ab8e0e67629e6456754a8c5dd8afe4b871c1f78d%7C1a59384a5e39b71ed21e460b99126c4f78f16ce3405f8bc0080a71298726d92d; __cf_bm=aPKrzkyE1z3GHcMd8zAya0CB4k0ZY8uqCXtB0H.4jvc-1670920176-0-ATLPhoXZQr90unJQa3Kc7Qgxof0CTQH1wUFAIyw9a2RvJ4WWD1XlwMrwr7jkOhEzv6eCFIkYdkzWX/mj89jxcmTsw94gk2xOPng5Fk06vVNrLY0o1+aJB6HFwcBpAlj3zpbXO47cIDKMiY63Q8dnuriuipQHzeUSZB+auUvDgd5kZQUzOHQh3zyqsDjoTN6fAw==; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..JmZtbrsgZh9xfUHo.BrivfSnt2cRygjYz67Icmcm0N-V3wpslXdyEYQwUhEaxpdRn6lQ3KSvnAvXO_CV7AvftYE7L6gjsZbCze3fXT_sQUMBCKTVNUxRQ_dm2Pkscnjgr61rTj6a6o_XgmbAAXVG11B1IOxq8_6aUO21_tm1fOEbwM7nS0ZJXRrqbnAxUlAc6iD9LIFswZbEVC1DTKdmf5ChyPI5--hG2R5DJQeexJd42GB-2V0zjli6SBIWehjGiEWbVZUh0OAoPRbwEsAIxMToPklX-GyD3K4TySbFkdwOGA5ej9sKZ7TO58N19TPtm19ub_dxbjAg54ujJ6x8B_7CiV1tUndC5Z1FbUgtqs78Hz9wvTYUS7Ha_Iwovj7dRfi8metTlH0H2FB953wNC4GNfBHDRM4-aI25hNLqvg_nDJJkaazDGVKUa2_j7gVE8NThMh6ClPCSev18rmey1felCW_wzdGnbM4KqrLiXVfWvYlijxNNia4Ubf7inYFXj9-bG8_hxa_BDrXcfISSo7BxwCSNXEiCvS8HJGfq9TPmj5e1dh5qu1ktdzLDzSqheAmpACqxpWyynv1f6CjJ3wSlSy1YU80r8hsktY_5QohK8tFaylHg3c41vk4_tVwLJwmzdUbDmHy4j9k_Ioxi4qKpJn8dFB3ijupBYTqNr4AgfPa78MCAHuXsQl1_2-0PJvHnf9GvYpa6R7LcV4l2HW1rZ1GoByW1-dQF7OaBqLLMaY2sooz0v5yc81nzGNRwNGojJusloOoeqcpRxOsbPB9F4mBqaSNp_5pnvS1aPXcEaf_aZBRMahbM5TBz-29ySnpLSXe98H9ewGH2UtG6g_2qyRIndIkBKV4JTl-apq00CbpJsz1HEf5UFMTNUAXR1acObEO3N0CxamOtVgEVRejTIQI5soO6x5mFVx7Nza1-s5VJDJbFNszTzVrR4PSgovZMQse_eLQRjRfFsQELkyBTiO2lF_ltD6cSOBDaJQUkiaG5vptFjeI3KQ48z1DvbQYmOml3-LHHFOYek35uwGcPGrAbv_kjl9HrX-X3x6dDy8bTB1GGvvjbvf7DW6JXi5yMEf9pFp0dFV1t0aBEmAVeE7kANbSXsuRkkbVPrPcUyF44zwRf2b3njMhx0H7ppj1c6cKxusDWKIvGRH0PycMGhxS-H96bGvdT5Cv2jDWwBFby-BvpZRKpsnQHamS7EXSM9rgA2560g1hDRNhNtJ94LVCjf2a86wIydnnYaBW8cq227NIriuZhJAkGrM5Kfb9F_ZLQWZGt2hCvmPInYBryj0SkGAZq-Bd9TDSFVuPsmOnrzO7koEun-JGwqOxnfuQSDmDJ8tFkRQ5ykfUrPxZ6NmKU9Y0pB1PJc06v0X2AxpC0FeWiwk7lTBVnQ-Mii9poQqmlXvBlOs6BoA_-ciDU8y4336CXklYOW9wNyWI2oiCyZ0I2LeHhMzBlGaDM1E9Dg7YtV5x1C_EihYngeXRgQRe6j1Drjk-a7MxmdpKwef_nmxkpcOsCzxVNkl_hVe0KmXnc1lulxPIaq-UJaPj0PiL6dKRQmagtD0So0wIuISpmbMbxRemAATGXTtaiZMuf46bauRZThraObfzvEBUkeNc8LxpKJ7Y2WT3AmAsQ8qyEvuskq8lcOn1Q0PGmYLFppSCOT_gJCKH8ZXa0PVZqpFB9imkYPUy0LKCXuFJX75suAq2tgbFlTPU5lOgc92opD-6iXRKbB8RxcOUu_QrPbBldr9wI4zWzMSytYXNUOEc2w7ajfnG3ARV7HEuxwLimbrcHdkaIIGYPQIptosXyQABLP8qNu0tmBLlZgDZYXqj5Qr8rRyLNZhT5XSrGARMw2mOIOenQ4ydRDlaQUtcS9xSFiRyn7Crqrbmhe8en7b-eNhqpi145EUvfhe_kkUFsYCyWFIIFvZXJQcvAFT59LZgMXwmpq8VwKEpc8015sjueSgvxImktjUCfAEFagRbQ6srlVyvNJurlFB3_nNyIJ8qbBaj5ohcOYpE2thU5lTvUe6cgoAogaimBa2j9a3uFB86iYDdc-6sQBbbkGbi_nG64i8BWYKCUZDZhtiih5QWGrOKohs600nn1Z5Mf96h55WiL7HTDN0A1-P8mA5L98TsfYvB-OzjppfRczI8URwhZF28m_3NKJMfUb62mE2hzGrmSeggeicOjviZdOPLiO0vZ8xEHPm8UG3lsre5-M2ksnnSyKe3s9lmF6sOBfIJpKlToHQF0HmMovrdUbbfhvpv0eq08OoMQKEJLR5GBMXw-rdzr2BOKtQ3XST8MLn3_tI9CovcDdKdKqOqDT8_Ms1vX6DvGyHRiPePUCoEMvCR-rPPz7veZ25RZZOsQSNkpQSGI.ZSdu8f_Z3Ystd5Gbnk4KqA', 'referer': 'https://chat.openai.com/chat', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"macOS"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
import json

# print(a['user-agent'])

from playwright.sync_api import sync_playwright
from cf_clearance import sync_cf_retry, sync_stealth
import requests

# not use cf_clearance, cf challenge is fail
proxies = {
    "all": "http://127.0.0.1:6152"
}
res = requests.get('https://nowsecure.nl', proxies=proxies)
if '<title>Please Wait... | Cloudflare</title>' in res.text:
    print("cf challenge fail")
# get cf_clearance
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, proxy={"server": "http://127.0.0.1:6152"})
    page = browser.new_page()
    sync_stealth(page, pure=True)
    page.goto('https://chat.openai.com/chat')
    res = sync_cf_retry(page)
    if res:
        cookies = page.context.cookies()
        for cookie in cookies:
            if cookie.get('name') == 'cf_clearance':
                cf_clearance_value = cookie.get('value')
                print(cf_clearance_value)
        ua = page.evaluate('() => {return navigator.userAgent}')
        print(ua)
    else:
        print("cf challenge fail")
    browser.close()
# use cf_clearance, must be same IP and UA
headers = {"user-agent": ua}
cookies = {"cf_clearance": cf_clearance_value}

#
config = {
    "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..K0DtQGnAq0I1AIKz.tE4fSlFsQXxeVQItta6rZC0ZE4srl1Vv34Dy0JWIu2V9DVQKWVnWSJ7HeXSsTsudcLksS4O6o75-XtsGfHu6gO9_zo0zMmcX9YCe8wLzUls9NFHiKl_SVifQ5sXC8YKf0jTKQx5b0WZpIYvqEZg92n7yFPPRIbu69EfhoJD5gjAMl_iwNFm3xhVk6vQTBAEuvP9twiAOWJaT04Zt40KGWg-R-XlJbmRITIIUogGz9XQ5SCu6OJR4f4cmMEXx5ln4TsSc3Y9T7XTFJSuDftXC6M3Ue1_BYjhDlKhpR2IswQyE_6L6LJ3XkbKIECb21ubhPsJnDQThoQF1PqxWDWPpBmAg-mK-7tlthIJlSg0bhCOgrmhTP1-xl_8cTuKrHDUNtY_iAz6Ie1j0UpqtcKMOsZRM4uXo2AzLRKMQysQw3DpvvV-kRBp-eEg_tbo7uJD_mRdylBk575-puY4p6GwgoXBtZxEgvNkTD-VVzgLC9Is5_NYYx0668uwrwbGqpI4YuvzCS801-uqVx8WrWJCKOp4DFt3w6c5ifBxtC_Gwuyc32BaaJb9ijQ9S902-LuXgJ69YaqT612sKhy5y_KNCFiCBifEkcmetn-zHo9thcKD8Y6Fbc_ce_GRIdx_qtTzP3Z7LPr_XRAyca5ecEyi4Ow-w1Mhw9fR7nQw4nojThL8E62KefNqmi11EM73JVzez6JB5DXE2-bN38BS0oxrDEKzfpBuRHTQXDMT-DFWwjN1v6PgZ0WgItbG7cCtR5Okj3tbDSGgZVtD80JLDk52bL6vJHq1qsmv18NmRJMAoatfRPrHVwdgYwAKjtPRv3CxRKJ4tygjM1tXiKkP88-mUuWmeQkD2ZRa7-DrbWcfjEYpcYnqrpkYJPclrS7sJ_-WlX6iIF-DnB6j_ByosPq1kVIJ12CyWuyUShPy5hjZN6TJ0OKN00hPGEOlG70832Oj0RLwGNLFtitna6Mi-E4Eo6C4RfLviYyBUlyPr0-9Q-LygN0hqxNLETvv2jTs6NclNrwcd6en5locMf3yXi3lx1ZOtC4RM6-Zpo9gp4Dcnopui2I403mcobXTAivdursq5Da45FLLibr7qh_9MLfc41CBVmXldO5Qb3S8JgNXvU-Mxy3o6IXjDRy9NFz4QSRf4ZV0pS7VQEI-zmyK772zK_0w86V98i93JOmWg_N0hPXyu-p5eRCUeYzQmuuf_-mgkkszlk2-RNe6oaVrH_4Q3s1o9mtURvm8usyAKPdopOR61luvX1hmxYWfwTyBLhxktjvOm81BE1OJb5ogOX5DEJgLQYr27XXkv_R9tfD3KTlscOH1zNDVT3YARjJROPl-OrPgf9gre6KEiiqpZ3JKeK1NITdinU4QpFQl4yXZ22-sxEO9lQA-PHXd8GbjEqFaar2rPrVP3HcgnIy33VMWqqJtzPtNsGeihd8NEJhIEhrUkRSgO1uSZ4EwHGSUTflJ7kQyVyPiR2eXh9aejYRECB1NP7mZ2L7NCaMWfOgzF2o5nuaSbH9hMOhjHrYHDCJtP4M8ir0_6SE4mB4DtAJWB3PA-4lf__AQgc4W9uVGPVXKkFYy25HRmej_ZGj1d7HiZfFkAIu27cIjlmoHEQETdfvgWqLCyZ3KOq_DsccitEsSJGVrq1_ynVpg33j7ACZFithllCN_4TfIMp-Nsr23WEZWyByco4sjjDx4gTBuXEY9yax0-17Y1UClSRgf7e5NVdpEywC3WyM8HzuERF3Ta83bFsVszcX9TBuHm3L_8shw3RGPSqn4Yl3LsoIMaYLPHy-7El9kcCvO7ZzsV9ezCZAYR6evZVb6trrdJEpOzWeS0h6GjXdVK4mZ6qVUt7IjYxIv0SACVgvoIcX4WAViRLsE6EQB2_GesYwEwbhROK-BPmYeMcPIMvNjQKw_7um5CK3P6Ji5dBcjVfTQNkxMyFU3zLXnD-j0Xvh6SMOh7cL_ldJo_NVDHYJo0CfV7Mbnpvjp4w8TAyQmiLiIR5eXXKtqcs7XUjeZt3Gy6k3799zLorMsrZgtW4albkAVPU9wT8PW2gE9A15iXeiVHx_04G89CZfeGFOdTPANFg7yyiRlVcinol9AEDuLsONbpgkYJFv7oPPeGxWtTakdbGUr1D8vBtcxHhxJy5e8Mszw9iEg2YH_jDybeGGsoYtomIr_olJPbUJi38uW9Xh4xWGB3kKxbMoqejZzUBKyYSjM5hbv2qlTQteaElIn82ZZqV4VtLjYUo5sJfAFC5Q.haBW7QU4-Z4TeSdqqpmPvQ",
    "cf_clearance": cf_clearance_value,
    "user-agent": ua,
    "proxy": "http://127.0.0.1:6152"
}
print(config)
chatbot = Chatbot(config, conversation_id=None)
#
res = chatbot.get_chat_response("hello")
print(res)

res = chatbot.get_chat_response("继续")
print(res)
# res = requests.get('https://nowsecure.nl', proxies=proxies, headers=headers, cookies=cookies)
# if '<title>Please Wait... | Cloudflare</title>' not in res.text:
#     print("cf challenge success")
#

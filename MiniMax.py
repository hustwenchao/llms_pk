from LLM import LLMBase

import configparser

model_list = [
    'abab6.5s-chat',
]


class MaxMini(LLMBase):
    def __init__(self):
        super().__init__()
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_key = config['api']['mini_max_api_secret']
        self.group_id = config['api']['mini_max_group_id']
        print("api_key", self.api_key)
        print("group_id", self.group_id)

    def test_openai(self):
        # OpenAI 的接口写法
        from openai import OpenAI

        client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.minimax.chat/v1",
            default_headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        completion = client.chat.completions.create(
            model="abab6.5s-chat",
            messages=[
                {"role": "system",
                 "content": "MM智能助理是一款由MiniMax自研的，没有调用其他产品的接口的大型语言模型。MiniMax是一家中国科技公司，一直致力于进行大模型相关的研究。"},
                {"role": "user", "content": "你好"}
            ]
        )

        print(completion)
        print("Trace-ID:", completion.id)

    def test(self):
        # 类似于原生的requests的写法调用
        import requests

        url = f"https://api.minimax.chat/v1/text/chatcompletion_v2?GroupId={self.group_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        print(headers)
        payload = {
            "model": "abab6.5s-chat",
            "messages": [
                {
                    "role": "system",
                    "name": "MM智能助理",
                    "content": "MM智能助理是一款由MiniMax自研的，没有调用其他产品的接口的大型语言模型。MiniMax是一家中国科技公司，一直致力于进行大模型相关的研究。"
                },
                {
                    "role": "user",
                    "name": "用户",
                    "content": "111"
                },
            ],
            "tools": [],
            "tool_choice": "none",
            "stream": False,
            "max_tokens": 256,
            "temperature": 0.1,
            "top_p": 0.95
        }

        response = requests.post(url, headers=headers, json=payload)

        print(response.status_code)
        print(response.text)

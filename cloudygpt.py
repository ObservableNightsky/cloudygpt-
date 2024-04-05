import requests
import json
import getpass
import base64
import os

class CloudyGpt:
    def __init__(self):
        self.url = "https://api.promptboom.com/requestPowerChat"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition std-1)",
            "authority": "api.promptboom.com",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "email": "",
            "isprouser": "false",
            "origin": "https://promptboom.com",
            "pragma": "no-cache",
            "referer": "https://promptboom.com/",
            "sec-ch-ua": "\"Not A(Brand)\";v=\"99\", \"Opera GX\";v=\"107\", \"Chromium\";v=\"121\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "token": ""
        }
        self.user = getpass.getuser()
        self.conversation_histories = []

    def encode_conversation_history(self, history):
        encoded_history = base64.b64encode(json.dumps(history).encode()).decode()
        return encoded_history

    def add_to_conversation(self, history, role, content):
        history["chatList"].append({"role": role, "content": content})
        return history

    def initiate_conversation(self):
        conversation_history = {
            "did": "6f87cd9d50fb20c2b41fa64f7d01c392",
            "chatList": [],
            "botID": "default",
            "special": {
                "referer": "https://github.com/LiLittleCat/awesome-free-chatgpt/blob/main/README_en.md",
                "path": "https://promptboom.com/PowerChat/PowerChatTalk"
            }
        }
        return conversation_history

    def send_user_input(self, user_input, conversation_history):
        conversation_history = self.add_to_conversation(conversation_history, "user", user_input)
        encoded_data = self.encode_conversation_history(conversation_history)
        data = {"data": encoded_data}
        response = requests.post(self.url, headers=self.headers, json=data)
        conversation_history = self.add_to_conversation(conversation_history, "assistant", response.text)
        self.conversation_histories.append(conversation_history)
        return response.text
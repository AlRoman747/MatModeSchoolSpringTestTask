import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("APIKEY")
URL = os.getenv("ENDPOINT")
MODEL = "qwen3.5-122b"


class LLMClient:
    def __init__(self, endpoint: str = URL, api_key: str = API_KEY, model: str = MODEL, history_enabled: bool = False):
        self.endpoint = endpoint
        self.api_key = api_key
        self.model = model
        self.history_enabled = history_enabled
        self.messages = []


    def reset_history(self):
        self.messages = []

    def ask(self, prompt: str):

        if self.history_enabled:
            self.messages.append({"role": "user", "content": prompt})
            messages = self.messages
        else:
            messages = [{"role": "user", "content": prompt}]

        payload = {
            "model": self.model,
            "messages": messages
        }

        headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(
            self.endpoint,
            headers=headers,
            json=payload
        )

        response.raise_for_status()

        answer = response.json()["choices"][0]["message"]["content"]

        if self.history_enabled:
            self.messages.append({"role": "assistant", "content": answer})
        return answer
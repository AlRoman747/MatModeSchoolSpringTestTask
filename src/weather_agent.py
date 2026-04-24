import os
import requests
import re
from dotenv import load_dotenv
from llm_client import LLMClient

load_dotenv()

def extract_city(message: str) -> str | None:
    llm = LLMClient()
    res = llm.ask(f"name city from {message}. One word. Only city, noting more. If it not full name, try give full name of city.")
    return res

class WeatherTool:
    name = "weather"
    description = "Отвечает на вопросы о погоде"

    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.url = "http://api.weatherapi.com/v1/current.json"

    def can_handle(self, message: str) -> bool:
        llm = LLMClient()
        res = llm.ask(f"is it question about weather? {message} \n if yes, print yes, else no. Only yes or no. Nothing more.")
        return 'yes' in res

    def run(self, message: str) -> str:
        city = extract_city(message)

        params = {
            "key": self.api_key,
            "q": city,
            "lang": "ru"
        }

        try:
            response = requests.get(self.url, params=params)
            data = response.json()

            if "error" in data:
                return f"Ошибка: {data['error']['message']}"

            temp = data["current"]["temp_c"]
            feels = data["current"]["feelslike_c"]
            condition = data["current"]["condition"]["text"]

            return (
                f"{city}:\n"
                f"Температура: {temp}C\n"
                f"Ощущается как: {feels}C\n"
                f"Состояние: {condition}"
            )

        except Exception:
            return "Ошибка при запросе к сервису погоды"
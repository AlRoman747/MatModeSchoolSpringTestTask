class WeatherTool:
    name = "weather"
    description = "Отвечает на вопросы о погоде"

    def can_handle(self, message: str) -> bool:
        keywords = ["погода", "температура", "дождь", "weather"]
        return any(k in message.lower() for k in keywords)

    def run(self, message: str) -> str:
        return "Сейчас примерно +15°C, облачно"
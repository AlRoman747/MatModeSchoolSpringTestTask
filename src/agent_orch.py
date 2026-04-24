from src.llm_client import LLMClient
from src.tools_protocols import Tool


class AgentOrchestrator:
    def __init__(self, llm: LLMClient, tools: list[Tool]):
        self.llm = llm
        self.tools = tools

    def route(self, message: str):
        for tool in self.tools:
            if tool.can_handle(message):
                return tool
        return None

    def ask(self, message: str) -> str:
        tool = self.route(message)

        if tool:
            tool_result = tool.run(message)

            prompt = f"""
Пользователь спросил: {message}
Инструмент вернул: {tool_result}
Сформулируй ответ.
"""
            return self.llm.ask(prompt)

        return self.llm.ask(message)
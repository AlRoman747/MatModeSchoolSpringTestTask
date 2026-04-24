from src.llm_client import LLMClient
from src.weather_agent import WeatherTool
from src.agent_orch import AgentOrchestrator


llm = LLMClient(history_enabled=True)

tools = [
    WeatherTool(),
]

agent = AgentOrchestrator(llm, tools)


while text := input():
    print(agent.ask(text))
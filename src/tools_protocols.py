from typing import Protocol


class Tool(Protocol):
    name: str
    description: str

    def can_handle(self, query: str) -> bool:
        """Как """
        ...

    def run(self, query: str) -> str:
        ...
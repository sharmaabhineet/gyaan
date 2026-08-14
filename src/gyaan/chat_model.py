from typing import Protocol


class ChatModel(Protocol):
    def generate(self, prompt: str) -> str:
        """Generate a response for the provided prompt."""
        pass

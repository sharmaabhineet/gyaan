from ollama import Client

from gyaan.chat_model import ChatModel


class OllamaModel(ChatModel):
    def __init__(
        self,
        client: Client,
        model: str,
    ) -> None:
        self._client = client
        self._model = model

    def generate(self, prompt: str) -> str:
        response = self._client.generate(
            model=self._model,
            prompt=prompt,
        )

        if response.response is None:
            raise ValueError("Ollama returned no response text")

        return response.response

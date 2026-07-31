from openai import OpenAI

from gyaan.chat_model import ChatModel


class OpenAIModel(ChatModel):
    def __init__(
        self,
        client: OpenAI,
        model: str,
    ) -> None:
        self._client = client
        self._model = model

    def generate(self, prompt: str) -> str:
        response = self._client.responses.create(
            model=self._model,
            input=prompt,
        )

        return response.output_text

from openai import OpenAI


class OpenAIModel:
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

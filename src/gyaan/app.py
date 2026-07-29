from gyaan.chat_model import ChatModel


class GyaanApplication:
    def __init__(self, model: ChatModel) -> None:
        self._model = model

    def run(self, prompt: str) -> str:
        return self._model.generate(prompt)

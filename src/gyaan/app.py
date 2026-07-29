from gyaan.chat_model import ChatModel


class GyaanApplication:
    def __init__(self, model: ChatModel) -> None:
        self._model = model

    def run(self) -> None:
        response = self._model.generate("What makes a system AI-native?")
        print(response)

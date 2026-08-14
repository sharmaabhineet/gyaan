from gyaan.chat_model import ChatModel


class StubChatModel:
    def generate(self, prompt: str) -> str:
        return f"Response to: {prompt}"


def use_model(model: ChatModel) -> str:
    return model.generate("What is AI-native?")


def test_chat_model_protocol_accepts_compatible_implementation() -> None:
    model = StubChatModel()

    result = use_model(model)

    assert result == "Response to: What is AI-native?"

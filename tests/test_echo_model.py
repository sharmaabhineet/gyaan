from gyaan.chat_model import ChatModel
from gyaan.echo_model import EchoModel


def use_model(model: ChatModel) -> str:
    return model.generate("What makes a system AI-native?")


def test_echo_model_returns_prompt_with_prefix() -> None:
    model = EchoModel()

    response = use_model(model)

    assert response == "Echo: What makes a system AI-native?"

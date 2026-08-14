from unittest.mock import Mock

from gyaan.app import GyaanApplication
from gyaan.chat_model import ChatModel


def test_application_sends_constructed_prompt_to_model() -> None:
    model = Mock(spec=ChatModel)
    model.generate.return_value = "A generated response"
    application = GyaanApplication(model)

    response = application.run("What makes a system AI-native?")

    model.generate.assert_called_once()
    sent_prompt = model.generate.call_args.args[0]
    assert "What makes a system AI-native?" in sent_prompt
    assert sent_prompt != "What makes a system AI-native?"
    assert response == "A generated response"

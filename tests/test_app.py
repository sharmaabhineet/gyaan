from unittest.mock import Mock

from gyaan.app import GyaanApplication
from gyaan.chat_model import ChatModel


def test_application_generates_response_for_prompt() -> None:
    model = Mock(spec=ChatModel)
    model.generate.return_value = "A generated response"
    application = GyaanApplication(model)

    response = application.run("What makes a system AI-native?")

    model.generate.assert_called_once_with("What makes a system AI-native?")
    assert response == "A generated response"

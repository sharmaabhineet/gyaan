from unittest.mock import Mock

from _pytest.capture import CaptureFixture

from gyaan.app import GyaanApplication
from gyaan.chat_model import ChatModel


def test_application_generates_and_prints_response(
    capsys: CaptureFixture[str],
) -> None:
    model = Mock(spec=ChatModel)
    model.generate.return_value = "A generated response"
    application = GyaanApplication(model)

    application.run()

    model.generate.assert_called_once_with("What makes a system AI-native?")
    captured = capsys.readouterr()
    assert captured.out == "A generated response\n"

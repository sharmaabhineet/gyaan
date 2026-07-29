from unittest.mock import Mock, patch

from _pytest.capture import CaptureFixture

from gyaan.main import main


@patch("gyaan.main.GyaanApplication")
@patch("gyaan.main.EchoModel")
def test_main_passes_prompt_to_application(
    model_class: Mock,
    application_class: Mock,
    capsys: CaptureFixture[str],
) -> None:
    model = model_class.return_value
    application = application_class.return_value
    application.run.return_value = "A generated response"

    main(["What makes a system AI-native?"])

    model_class.assert_called_once_with()
    application_class.assert_called_once_with(model)
    application.run.assert_called_once_with("What makes a system AI-native?")

    captured = capsys.readouterr()
    assert captured.out == "A generated response\n"

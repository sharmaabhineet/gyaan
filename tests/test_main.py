from unittest.mock import Mock, patch

from gyaan.main import main


@patch("gyaan.main.GyaanApplication")
@patch("gyaan.main.EchoModel")
def test_main_wires_echo_model_into_application(
    model_class: Mock,
    application_class: Mock,
) -> None:
    model = model_class.return_value
    application = application_class.return_value

    main()

    model_class.assert_called_once_with()
    application_class.assert_called_once_with(model)
    application.run.assert_called_once_with()

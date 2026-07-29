from unittest.mock import Mock, patch

from gyaan.main import main


@patch("gyaan.main.GyaanApplication")
def test_main_runs_application(
    application_class: Mock,
) -> None:
    application = application_class.return_value

    main()

    application_class.assert_called_once_with()
    application.run.assert_called_once_with()

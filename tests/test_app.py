from _pytest.capture import CaptureFixture

from gyaan.app import GyaanApplication


def test_application_prints_ready_message(
    capsys: CaptureFixture[str],
) -> None:
    application = GyaanApplication()

    application.run()

    captured = capsys.readouterr()
    assert captured.out == "Gyaan assistant is ready.\n"

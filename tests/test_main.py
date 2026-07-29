from _pytest.capture import CaptureFixture

from gyaan.main import main


def test_main_prints_ready_message(capsys: CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "Gyaan assistant is ready.\n"

from unittest.mock import Mock

import pytest

from gyaan.app import GyaanApplication
from gyaan.main import create_application, main, parse_args


def test_parse_args_returns_prompt() -> None:
    args = parse_args(["What makes a system AI-native?"])

    assert args.prompt == "What makes a system AI-native?"


def test_main_prints_application_response(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    application = Mock(spec=GyaanApplication)
    application.run.return_value = "A model-generated response."

    monkeypatch.setattr(
        "gyaan.main.create_application",
        lambda: application,
    )

    main(["What makes a system AI-native?"])

    captured = capsys.readouterr()

    application.run.assert_called_once_with("What makes a system AI-native?")
    assert captured.out == "A model-generated response.\n"


def test_create_application_uses_echo_model_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    echo_model = Mock()
    application = Mock()

    echo_model_factory = Mock(return_value=echo_model)
    application_factory = Mock(return_value=application)

    monkeypatch.delenv("GYAAN_PROVIDER", raising=False)
    monkeypatch.setattr(
        "gyaan.main.EchoModel",
        echo_model_factory,
    )
    monkeypatch.setattr(
        "gyaan.main.GyaanApplication",
        application_factory,
    )

    result = create_application()

    echo_model_factory.assert_called_once_with()
    application_factory.assert_called_once_with(echo_model)
    assert result is application


def test_create_application_uses_openai_model(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("GYAAN_PROVIDER", "openai")
    monkeypatch.setenv("GYAAN_MODEL", "test-model")

    client = Mock()
    openai_model = Mock()
    application = Mock()

    openai_client_factory = Mock(return_value=client)
    openai_model_factory = Mock(return_value=openai_model)
    application_factory = Mock(return_value=application)

    monkeypatch.setattr(
        "gyaan.main.OpenAI",
        openai_client_factory,
    )
    monkeypatch.setattr(
        "gyaan.main.OpenAIModel",
        openai_model_factory,
    )
    monkeypatch.setattr(
        "gyaan.main.GyaanApplication",
        application_factory,
    )

    result = create_application()

    openai_client_factory.assert_called_once_with()
    openai_model_factory.assert_called_once_with(
        client=client,
        model="test-model",
    )
    application_factory.assert_called_once_with(openai_model)
    assert result is application


def test_create_application_uses_ollama_model(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("GYAAN_PROVIDER", "ollama")
    monkeypatch.setenv("GYAAN_MODEL", "test-model")

    client = Mock()
    ollama_model = Mock()
    application = Mock()

    ollama_client_factory = Mock(return_value=client)
    ollama_model_factory = Mock(return_value=ollama_model)
    application_factory = Mock(return_value=application)

    monkeypatch.setattr(
        "gyaan.main.OllamaClient",
        ollama_client_factory,
    )
    monkeypatch.setattr(
        "gyaan.main.OllamaModel",
        ollama_model_factory,
    )
    monkeypatch.setattr(
        "gyaan.main.GyaanApplication",
        application_factory,
    )

    result = create_application()

    ollama_client_factory.assert_called_once_with()
    ollama_model_factory.assert_called_once_with(
        client=client,
        model="test-model",
    )
    application_factory.assert_called_once_with(ollama_model)
    assert result is application


def test_create_application_rejects_unknown_provider(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("GYAAN_PROVIDER", "unknown")

    with pytest.raises(
        ValueError,
        match="Unsupported model provider: unknown",
    ):
        create_application()

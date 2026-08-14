from unittest.mock import Mock

import pytest
from ollama import Client

from gyaan.ollama_model import OllamaModel


def test_generate_returns_response_text() -> None:
    client = Mock(spec=Client)

    response = Mock()
    response.response = "Hello!"

    client.generate.return_value = response

    model = OllamaModel(
        client=client,
        model="llama3",
    )

    assert model.generate("Hi") == "Hello!"

    client.generate.assert_called_once_with(
        model="llama3",
        prompt="Hi",
    )


def test_generate_raises_when_response_is_none() -> None:
    client = Mock(spec=Client)

    response = Mock()
    response.response = None

    client.generate.return_value = response

    model = OllamaModel(
        client=client,
        model="llama3",
    )

    with pytest.raises(ValueError, match="Ollama returned no response text"):
        model.generate("Hi")

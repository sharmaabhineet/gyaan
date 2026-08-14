from unittest.mock import Mock

from openai import OpenAI

from gyaan.openai_model import OpenAIModel


def test_generate_returns_output_text() -> None:
    client = Mock(spec=OpenAI)

    response = Mock()
    response.output_text = "Hello!"

    client.responses.create.return_value = response

    model = OpenAIModel(
        client=client,
        model="gpt-5.5",
    )

    assert model.generate("Hi") == "Hello!"

    client.responses.create.assert_called_once_with(
        model="gpt-5.5",
        input="Hi",
    )

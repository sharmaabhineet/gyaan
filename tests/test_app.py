from unittest.mock import Mock

from gyaan.app import GyaanApplication
from gyaan.chat_model import ChatModel
from gyaan.research_prompt import ResearchPrompt, ResearchPromptInput


def test_application_sends_rendered_prompt_to_model() -> None:
    model = Mock(spec=ChatModel)
    prompt = ResearchPrompt()
    application = GyaanApplication(model, prompt)

    application.run("What makes a system AI-native?")

    model.generate.assert_called_once_with(
        prompt.build(ResearchPromptInput(question="What makes a system AI-native?"))
    )


def test_application_returns_the_models_response() -> None:
    model = Mock(spec=ChatModel)
    model.generate.return_value = "A generated response"
    application = GyaanApplication(model, ResearchPrompt())

    response = application.run("What makes a system AI-native?")

    assert response == "A generated response"

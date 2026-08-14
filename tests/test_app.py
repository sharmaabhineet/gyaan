from unittest.mock import Mock

from gyaan.app import GyaanApplication
from gyaan.chat_model import ChatModel
from gyaan.research_prompt import ResearchPrompt


def test_application_sends_rendered_prompt_to_model() -> None:
    model = Mock(spec=ChatModel)
    model.generate.return_value = "A generated response"
    prompt = ResearchPrompt()
    application = GyaanApplication(model, prompt)

    response = application.run("What makes a system AI-native?")

    model.generate.assert_called_once_with(
        prompt.build("What makes a system AI-native?")
    )
    assert response == "A generated response"

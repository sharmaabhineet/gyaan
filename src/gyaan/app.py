from gyaan.chat_model import ChatModel
from gyaan.research_prompt import ResearchPrompt


class GyaanApplication:
    def __init__(self, model: ChatModel, prompt: ResearchPrompt) -> None:
        self._model = model
        self._prompt = prompt

    def run(self, question: str) -> str:
        rendered_prompt = self._prompt.build(question)
        return self._model.generate(rendered_prompt)

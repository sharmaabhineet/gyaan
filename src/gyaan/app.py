from gyaan.chat_model import ChatModel
from gyaan.research_prompt import ResearchPrompt, ResearchPromptInput


class GyaanApplication:
    def __init__(self, model: ChatModel, prompt: ResearchPrompt) -> None:
        self._model = model
        self._prompt = prompt

    def run(self, question: str) -> str:
        prompt_input = ResearchPromptInput(question=question)
        rendered_prompt = self._prompt.build(prompt_input)
        return self._model.generate(rendered_prompt)

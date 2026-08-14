from gyaan.chat_model import ChatModel


class GyaanApplication:
    def __init__(self, model: ChatModel) -> None:
        self._model = model

    def run(self, question: str) -> str:
        prompt = self._build_prompt(question)
        return self._model.generate(prompt)

    def _build_prompt(self, question: str) -> str:
        return (
            "You are Gyaan, a research assistant.\n"
            "Answer the following question clearly and accurately.\n\n"
            f"Question:\n{question}"
        )

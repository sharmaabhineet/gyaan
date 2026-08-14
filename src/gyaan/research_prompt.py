class ResearchPrompt:
    def build(self, question: str) -> str:
        return (
            "You are Gyaan, a research assistant.\n"
            "Answer the following question clearly and accurately.\n\n"
            f"Question:\n{question}"
        )

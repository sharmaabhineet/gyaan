from dataclasses import dataclass


@dataclass(frozen=True)
class ResearchPromptInput:
    question: str
    context: str | None = None


class ResearchPrompt:
    def build(self, prompt_input: ResearchPromptInput) -> str:
        sections = [
            "You are Gyaan, a research assistant.\n"
            "Answer the following question clearly and accurately."
        ]

        if prompt_input.context:
            sections.append(f"Context:\n{prompt_input.context}")

        sections.append(f"Question:\n{prompt_input.question}")

        return "\n\n".join(sections)

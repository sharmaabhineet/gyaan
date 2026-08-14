from gyaan.research_prompt import ResearchPrompt


def test_build_includes_the_question() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build("What makes a system AI-native?")

    assert "What makes a system AI-native?" in rendered


def test_build_includes_application_instructions() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build("What makes a system AI-native?")

    assert "research assistant" in rendered.lower()

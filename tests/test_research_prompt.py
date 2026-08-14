from gyaan.research_prompt import ResearchPrompt, ResearchPromptInput


def test_build_includes_the_question() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build(
        ResearchPromptInput(question="What makes a system AI-native?")
    )

    assert "What makes a system AI-native?" in rendered


def test_build_includes_application_instructions() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build(
        ResearchPromptInput(question="What makes a system AI-native?")
    )

    assert "research assistant" in rendered.lower()


def test_build_includes_context_when_provided() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build(
        ResearchPromptInput(
            question="What makes a system AI-native?",
            context="Gyaan is built from first principles.",
        )
    )

    assert "Gyaan is built from first principles." in rendered


def test_build_omits_context_section_when_context_is_absent() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build(
        ResearchPromptInput(question="What makes a system AI-native?")
    )

    assert "Context" not in rendered


def test_build_places_context_before_question() -> None:
    prompt = ResearchPrompt()

    rendered = prompt.build(
        ResearchPromptInput(
            question="What makes a system AI-native?",
            context="Gyaan is built from first principles.",
        )
    )

    context_position = rendered.index("Gyaan is built from first principles.")
    question_position = rendered.index("What makes a system AI-native?")
    assert context_position < question_position

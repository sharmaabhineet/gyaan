import argparse
import os
from collections.abc import Sequence

from openai import OpenAI

from gyaan.app import GyaanApplication
from gyaan.chat_model import ChatModel
from gyaan.echo_model import EchoModel
from gyaan.openai_model import OpenAIModel


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask Gyaan a question.",
    )

    parser.add_argument(
        "prompt",
        help="The prompt to send to the model.",
    )

    return parser.parse_args(args)


def create_application() -> GyaanApplication:
    provider = os.getenv("GYAAN_PROVIDER", "echo")

    model: ChatModel

    if provider == "echo":
        model = EchoModel()
    elif provider == "openai":
        client = OpenAI()
        model = OpenAIModel(
            client=client,
            model=os.environ["GYAAN_MODEL"],
        )
    else:
        raise ValueError(f"Unsupported model provider: {provider}")

    return GyaanApplication(model)


def main(args: Sequence[str] | None = None) -> None:
    parsed_args = parse_args(args)
    application = create_application()

    response = application.run(parsed_args.prompt)

    print(response)


if __name__ == "__main__":
    main()

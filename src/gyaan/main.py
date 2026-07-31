import argparse
import os
from collections.abc import Sequence

from openai import OpenAI

from gyaan.app import GyaanApplication
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
    model_name = os.environ["GYAAN_MODEL"]

    client = OpenAI()
    model = OpenAIModel(
        client=client,
        model=model_name,
    )

    return GyaanApplication(model)


def main(args: Sequence[str] | None = None) -> None:
    parsed_args = parse_args(args)
    application = create_application()

    response = application.run(parsed_args.prompt)

    print(response)


if __name__ == "__main__":
    main()

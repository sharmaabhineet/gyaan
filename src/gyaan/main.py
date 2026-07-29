import argparse
from collections.abc import Sequence

from gyaan.app import GyaanApplication
from gyaan.echo_model import EchoModel


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask Gyaan a question.",
    )
    parser.add_argument(
        "prompt",
        help="The prompt to send to the model.",
    )
    return parser.parse_args(args)


def main(args: Sequence[str] | None = None) -> None:
    parsed_args = parse_args(args)

    model = EchoModel()
    application = GyaanApplication(model)

    response = application.run(parsed_args.prompt)
    print(response)


if __name__ == "__main__":
    main()

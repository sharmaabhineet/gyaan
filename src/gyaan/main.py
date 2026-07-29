from gyaan.app import GyaanApplication
from gyaan.echo_model import EchoModel


def main() -> None:
    model = EchoModel()
    application = GyaanApplication(model)
    application.run()


if __name__ == "__main__":
    main()

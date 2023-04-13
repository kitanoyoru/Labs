import os

from argparse import ArgumentParser

from app import App


PROJECT_NAME = "lab1"
HOST = "localhost"
PORT = 8080


parser = ArgumentParser(prog=PROJECT_NAME, usage="%(prog)s [options]")
parser.add_argument(
    "--plants",
    help="How many plants simulation need to have",
    default=3,
)

args = parser.parse_args()

settings_path = os.path.join("config", ".env")

app = App.create_app(args.plants, settings_path)

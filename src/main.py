import logging
from argparse import ArgumentParser
from pathlib import Path

from src.files import Script
from src.types import ConfigFile


def setup_logger() -> None:

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def main() -> None:

    parser = ArgumentParser()
    parser.add_argument("file", help="Your project's setup config file", type=ConfigFile)
    args = parser.parse_args()
    setup_logger()
    cfg_file = args.file
    filepath = Path(".").resolve() / cfg_file.value

    script = Script(cfg_file, filepath)
    script.parse()
    script.scan()

    for cs in script.check():
        print(cs)


if __name__ == "__main__":
    main()

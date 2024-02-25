import logging
from argparse import ArgumentParser
from pathlib import Path

from src.files import Script
from src.types import ConfigFile
from src.util import setup_logger

logger = logging.getLogger(__name__)


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

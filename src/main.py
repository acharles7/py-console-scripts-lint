from argparse import ArgumentParser
from pathlib import Path

from src.files import parse_cfg_file
from src.types import ConfigFileType


def main() -> None:

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Your project's setup config file", type=ConfigFileType)

    args = parser.parse_args()

    cfg_file = args.file
    filepath = Path(".").resolve() / cfg_file.value
    parsed_cfg_file = parse_cfg_file(filepath, cfg_file)
    print("Parsed content:", parsed_cfg_file)


if __name__ == "__main__":
    main()

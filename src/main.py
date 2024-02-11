from argparse import ArgumentParser

from src.types import ConfigFileType
from src.files import parse_cfg_file


def main() -> None:

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Your project's main setup config file", type=ConfigFileType)

    args = parser.parse_args()
    parsed_cfg_file = parse_cfg_file(args.file)
    print(parsed_cfg_file)


if __name__ == "__main__":
    main()

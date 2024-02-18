from argparse import ArgumentParser
from pathlib import Path

from src.files import parse_cfg_file, scan_scripts
from src.types import ConfigFile


def main() -> None:

    parser = ArgumentParser()
    parser.add_argument("file", help="Your project's setup config file", type=ConfigFile)
    args = parser.parse_args()

    cfg_file = args.file
    filepath = Path(".").resolve() / cfg_file.value
    scripts = parse_cfg_file(filepath, cfg_file)
    print("Parsed content:", scripts)
    scripts_status = scan_scripts(scripts)
    for script in scripts_status:
        print(script)


if __name__ == "__main__":
    main()

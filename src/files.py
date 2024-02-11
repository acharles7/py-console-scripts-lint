from src.types import ConfigFileType


def parse_cfg_file(file: ConfigFileType) -> dict[str, str]:
    """Configuration file parser"""

    match file:
        case ConfigFileType.PYPROJECT:
            print("It's pyproject.toml")
        case ConfigFileType.SETUPPY:
            print("It's setup.py")
        case ConfigFileType.SETUPCFG:
            print("It's setup.cfg")
        case _:
            raise ValueError(f"Invalid file name '{file.value}'")

    return {}

from pathlib import Path

from src.types import ConfigFileType


def parse_setup_py_file(file: Path) -> dict[str, str]:
    # Fixme: Add support
    print(file)
    return {}


def parse_setup_cfg_file(file: Path) -> dict[str, str]:
    # Fixme: Add support
    print(file)
    return {}


def parse_pyproject_toml_file(file: Path) -> dict[str, str]:
    if file.exists():
        print(file)
    else:
        raise FileNotFoundError("File does not exists")
    return {}


def parse_cfg_file(filepath: Path, file: ConfigFileType) -> dict[str, str]:
    """Configuration file parser"""

    match file:
        case ConfigFileType.PYPROJECT:
            content = parse_pyproject_toml_file(filepath)
        case ConfigFileType.SETUPPY:
            content = parse_setup_py_file(filepath)
        case ConfigFileType.SETUPCFG:
            content = parse_setup_cfg_file(filepath)
        case _:
            raise ValueError(f"Invalid file name '{file.value}'")

    return content

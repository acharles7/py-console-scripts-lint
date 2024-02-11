from pathlib import Path

from src.types import ConfigFile


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


def parse_cfg_file(filepath: Path, file: ConfigFile) -> dict[str, str]:
    """Configuration file parser"""

    match file:
        case ConfigFile.PYPROJECT:
            content = parse_pyproject_toml_file(filepath)
        case ConfigFile.SETUPPY:
            content = parse_setup_py_file(filepath)
        case ConfigFile.SETUPCFG:
            content = parse_setup_cfg_file(filepath)
        case _:
            raise ValueError(f"Invalid file name '{file.value}'")

    return content

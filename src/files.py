from pathlib import Path
import tomllib
from src.types import ConfigFile, ConsoleScript, ScriptStatus


def parse_setup_py_file(file: Path) -> list[ConsoleScript]:
    # Fixme: Add support
    print(file)
    return []


def parse_setup_cfg_file(file: Path) -> list[ConsoleScript]:
    # Fixme: Add support
    print(file)
    return []


def parse_pyproject_toml_file(file: Path) -> list[ConsoleScript]:
    if not file.exists():
        raise FileNotFoundError(f"File '{file}' does not exist")

    with file.open("rb") as f:
        cfgs = tomllib.load(f)

    project = cfgs.get("project", {})
    scripts = project.get("scripts", {})
    return [ConsoleScript(name, script) for name, script in scripts.items()]


def parse_cfg_file(filepath: Path, file: ConfigFile) -> list[ConsoleScript]:
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


def scan_scripts(scripts: list[ConsoleScript]) -> list[ScriptStatus]:

    for script in scripts:
        print(script)

    return []

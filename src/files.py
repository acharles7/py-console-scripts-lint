from pathlib import Path
import tomllib
from src.types import ConfigFile, ConsoleScript, ScriptStatus


PYTHON_FILE_EXT = ".py"


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


def find_project_root_path() -> Path:
    return Path.cwd()


def convert_script_to_path(script: str) -> Path:
    cwd = find_project_root_path()
    parts, func = script.split(":")
    path = parts.replace(".", "/")
    final_path = (cwd / path).with_suffix(PYTHON_FILE_EXT)
    assert final_path.exists(), f"Console script path '{final_path}' does not exist"
    return final_path


def create_abs_script_path(script: ConsoleScript) -> Path:
    return convert_script_to_path(script.script)


def scan_scripts(scripts: list[ConsoleScript]) -> list[ScriptStatus]:
    for script in scripts:
        print(f"CHECKING {script.name}")
        try:
            script_path = create_abs_script_path(script)
            print(f"{script_path=}")
        except AssertionError as exc:
            print(f"ERROR: {exc}")

    return []

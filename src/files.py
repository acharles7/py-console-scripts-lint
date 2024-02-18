import tomllib
from pathlib import Path

from src.types import ConfigFile, ConsoleScript, ScriptMetadata, ScriptStatus

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


def convert_script_to_path(script: str) -> ScriptMetadata:
    cwd = find_project_root_path()
    parts, func = script.split(":")
    path = parts.replace(".", "/")
    final_path = (cwd / path).with_suffix(PYTHON_FILE_EXT)
    return ScriptMetadata(final_path, func)


def create_abs_script_path(script: ConsoleScript) -> ScriptMetadata:
    return convert_script_to_path(script.script)


def scan_scripts(scripts: list[ConsoleScript]) -> list[ScriptStatus]:
    scripts_metadata = []
    for script in scripts:
        metadata = create_abs_script_path(script)
        scripts_metadata.append(ScriptStatus(script, metadata))
    return scripts_metadata

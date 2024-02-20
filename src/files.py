import tomllib
from importlib import import_module
from pathlib import Path

from src.types import (
    ConfigFile,
    ConsoleScript,
    EnsureScriptStatus,
    EnsureScriptPathStatus,
    ErrorReason,
    ScriptMetadata,
    ScriptStatus,
    Status,
)

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


def generate_script_metadata(console_script: ConsoleScript) -> ScriptMetadata:
    cwd = find_project_root_path()
    parts, func = console_script.script.split(":")
    path = parts.replace(".", "/")
    final_path = (cwd / path).with_suffix(PYTHON_FILE_EXT)
    return ScriptMetadata(final_path, func, parts)


def scan_scripts(scripts: list[ConsoleScript]) -> list[ScriptStatus]:
    scripts_metadata = []
    for script in scripts:
        metadata = generate_script_metadata(script)
        scripts_metadata.append(ScriptStatus(script, metadata))
    return scripts_metadata


def ensure_scripts_exist(scripts: list[ScriptStatus]) -> list[EnsureScriptPathStatus]:
    """Checks for existence of all scripts"""
    script_status = []
    for script in scripts:
        path = script.metadata.path
        path_status = Status.from_bool(path.exists())
        script_status.append(EnsureScriptPathStatus(script.metadata, path_status))
    return script_status


def ensure_scripts_func_exists(scripts: list[ScriptStatus]) -> list[EnsureScriptStatus]:
    """Checks whether all scripts are runnable"""
    script_status = []

    for script in scripts:
        status = True
        error_reason = None
        module = script.metadata.package_path
        function = script.metadata.function
        try:
            file = import_module(module)
            getattr(file, function)
        except ModuleNotFoundError:
            print(f"Module '{module}' not found")
            status = False
            error_reason = ErrorReason.MODULE_NOT_FOUND
        except AttributeError:
            print(f"Function '{function}' not found")
            status = False
            error_reason = ErrorReason.MODULE_NOT_FOUND
        except Exception:
            print(f"Unexpected error")
            raise
        script_status.append(EnsureScriptStatus(script.metadata, Status.from_bool(status), error_reason))

    return script_status

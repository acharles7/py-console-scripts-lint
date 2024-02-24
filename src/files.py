import logging
import tomllib
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path

from src.types import ConfigFile, ConsoleScript, ErrorReason, ScriptInfo, ScriptMetadata, ScriptStatus, Status

PYTHON_FILE_EXT = ".py"

logger = logging.getLogger(__name__)


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


def find_project_root_path() -> Path:
    return Path.cwd()


def generate_script_metadata(console_script: ConsoleScript) -> ScriptMetadata:
    cwd = find_project_root_path()
    parts, func = console_script.script.split(":")
    path = parts.replace(".", "/")
    final_path = (cwd / path).with_suffix(PYTHON_FILE_EXT)
    return ScriptMetadata(final_path, func, parts)


@dataclass
class Script:

    config_file: ConfigFile
    config_file_path: Path

    def parse(self) -> list[ConsoleScript]:
        match self.config_file:
            case ConfigFile.PYPROJECT:
                content = parse_pyproject_toml_file(self.config_file_path)
            case ConfigFile.SETUPPY:
                content = parse_setup_py_file(self.config_file_path)
            case ConfigFile.SETUPCFG:
                content = parse_setup_cfg_file(self.config_file_path)
            case _:
                raise ValueError(f"Invalid file name '{self.config_file.value}'")
        self.scripts = content
        return self.scripts

    def scan(self) -> list[ScriptInfo]:
        scripts_metadata = []
        for script in self.scripts:
            metadata = generate_script_metadata(script)
            scripts_metadata.append(ScriptInfo(script, metadata))
        self.scripts_metadata = scripts_metadata
        return self.scripts_metadata

    def check(self) -> list[ScriptStatus]:
        script_status = []
        for script in self.scripts_metadata:
            status = True
            error_reason = None
            module = script.metadata.package_path
            function = script.metadata.function
            try:
                file = import_module(module)
                getattr(file, function)
            except ModuleNotFoundError:
                logger.error(f"Module '{module}' not found")
                status = False
                error_reason = ErrorReason.MODULE_NOT_FOUND
            except AttributeError:
                logger.error(f"Module '{module}' not found")
                status = False
                error_reason = ErrorReason.MODULE_NOT_FOUND
            except Exception:
                logger.exception("Unexpected error")
                raise
            script_status.append(ScriptStatus(script.metadata, Status.from_bool(status), error_reason))
        self.checked_scripts = script_status
        return self.checked_scripts

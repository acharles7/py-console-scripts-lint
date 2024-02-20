from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import NamedTuple


class ConfigFile(Enum):
    """The Python's project configuration file"""

    SETUPPY = "setup.py"
    SETUPCFG = "setup.cfg"
    PYPROJECT = "pyproject.toml"


class Status(Enum):
    """The status of the script"""

    OK = "OK"
    ERROR = "ERROR"

    @classmethod
    def from_bool(cls, value: bool) -> "Status":
        return Status.OK if value else Status.ERROR


class ErrorReason(Enum):

    UNKNOWN = "UNKNOWN"
    MODULE_NOT_FOUND = "MODULE_NOT_FOUND"
    FUNCTION_NOT_FOUND = "FUNCTION_NOT_FOUND"


@dataclass
class ConsoleScript:

    name: str
    script: str


class ScriptMetadata(NamedTuple):

    path: Path
    function: str
    package_path: str


@dataclass
class ScriptStatus:

    script: ConsoleScript
    metadata: ScriptMetadata


@dataclass
class EnsureScriptPathStatus:

    metadata: ScriptMetadata
    status: Status


@dataclass
class EnsureScriptStatus:

    metadata: ScriptMetadata
    status: Status
    error_reason: ErrorReason | None

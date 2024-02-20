from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import NamedTuple


class ConfigFile(Enum):
    """The standard Python's project configuration file"""

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
    """The error reason of the script"""

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
class ScriptInfo:

    script: ConsoleScript
    metadata: ScriptMetadata


@dataclass
class ScriptStatus:
    """A dataclass representing the status of a console script in the project"""

    metadata: ScriptMetadata
    status: Status
    error_reason: ErrorReason | None

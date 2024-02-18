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


@dataclass
class ConsoleScript:

    name: str
    script: str


class ScriptMetadata(NamedTuple):

    path: Path
    function: str


@dataclass
class ScriptStatus:

    script: ConsoleScript
    metadata: ScriptMetadata | None

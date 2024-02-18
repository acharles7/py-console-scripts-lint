from enum import Enum
from dataclasses import dataclass
from pathlib import Path


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


@dataclass
class ScriptStatus:

    script: ConsoleScript
    status: Status

from enum import Enum


class ConfigFile(Enum):
    """The Python's project configuration file"""

    SETUPPY = "setup.py"
    SETUPCFG = "setup.cfg"
    PYPROJECT = "pyproject.toml"

from enum import Enum


class ConfigFileType(Enum):
    """The Python's project configuration file"""

    SETUPPY = "setup.py"
    SETUPCFG = "setup.cfg"
    PYPROJECT = "pyproject.toml"

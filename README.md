# Python's Console Scripts Linter

## What is console script or entrypoints in Python?

Check out this official python documentation on [entry point.](https://setuptools.pypa.io/en/latest/userguide/entry_point.html)
Console script/ Entrypoints looks something like below code snippets and you probably may have interacted with this in your Python development career, Otherwise you won't be here :)

`pyproject.toml`
```toml
[project.scripts]
hello-world = "timmins:hello_world"
```

`setup.cfg`
```toml
[options.entry_points]
console_scripts =
    hello-world = timmins:hello_world
```

`setup.py`
```python
from setuptools import setup

setup(
    # ...,
    entry_points={
        'console_scripts': [
            'hello-world = timmins:hello_world',
        ]
    }
)
```

## The Problem

When we try to build the project using `pip install` . Python installer does not check whether console scripts exist or not and intentionally(?) create its binary in virtual environment.
Although, It does not create any issue. 

But, some engineer don't like this overhead in virtual environment and especially, when we remove dead code but forgot to remove it's entry from configuration file.  


## The Solution

`pip install TBD`

This package parse, scan, and check Python's configuration file

Basically, A linter which make sure script exists or not and suggest to remove if it's become obsolete.
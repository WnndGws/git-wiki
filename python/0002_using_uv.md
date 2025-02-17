---
title: 0002_using_uv
author: Wynand Gouws
date: 2024-12-04T14:56:49.000Z
public: true
---

- Create a virtual environment

```zsh
uv venv --python 3.13
source .venv/bin/activate
uv init
```

- Install toolchain (as needed)

```zsh
uv add addict pathlib tinydb orjson alive-progress anybadge loguru rich humanize arrow schedule pyspy configparser questionary typer httpx tenacity uv plumbum pydantic pyright regex thefuzz ruff robyn maturin polars pytest
```

- Can then run the file in the environment using `uv run python my_file.py`

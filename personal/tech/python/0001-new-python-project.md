---
title: 0001-new-python-project
author: Wynand Gouws
date: 2026-02-06 15:09:32
public: true
---

# Creating a new Python project

## General process

```zsh
$ mkdir project
$ cd project
$ uv init && uv venv && source .venv/bin/activate

## Edit the pyproject.toml file as below

$ mkdir -p src/{core,api,data,models,utils,config}
$ git-town init

## When and as needed
$ mkdir -p tests
$ mkdir -p docs/{api,usage}
$ mkdir -p config
```

## Editing the pyproject

* Add the following, then run `uv sync` to allow importing local modules

```toml
[tool.uv]
package = true
```

# References

* <https://medium.com/@adityaghadge99/python-project-structure-why-the-src-layout-beats-flat-folders-and-how-to-use-my-free-template-808844d16f35>
* <https://docs.astral.sh/uv/concepts/projects/config/#project-packaging>

---
title: 0007-precommit
author: Wynand Gouws
date: 2026-09-02 17:16:34
public: true
---

# Using pre-commit

> [!INFO]
> See [my boilerplate repo](https://github.com/wnndgws/boilerplate-repo) for how
> I have implemented this.
>
> The repo is almost certainly more up to date than the wiki

- These are more general tools to use alongside the normal linters in my nvim
  config

## Prek

- Install and init `prek` as per the documentation[^1]
- Use the following inbuilts:
  - trailing-whitespace
  - end-of-file-fixer
  - check-json
  - check-json5
  - check-toml
  - check-yaml
  - check-xml
  - check-merge-conflict
  - detect-private-key

## Tools to use

### Bandit

```yaml
repos:
  - repo: https://github.com/PyCQA/bandit
    rev: "" # Update me!
    hooks:
      - id: bandit
        args: ["-c", "pyproject.toml"]
        additional_dependencies: ["bandit[toml]"]
```

### Trufflehog

```toml
[[repos]]
repo = local
hooks = [
{
  id = "trufflehog",
  name = "TruffleHog",
  description = "Detect secrets in your data.", 
  entry = "bash -c 'trufflehog git file://.'", 
  language = "system",
  stages = ["pre-commit", "pre-push"]
}]

```

### Pyrefly

- Custom hook for pyrefly infer

```toml
[[repos]]
repo = "local"
hooks = [{
id = "pyrefly-infer",
name = "Pyrefly Infer (type annotation generation)",
entry = "pyrefly infer",
language = "system",
pass_filenames = true,
types = ["python"],
files = '^.*\.py$',
}]
```

- Then the official pyrefly-check

```yaml
repos:
  - repo: https://github.com/facebook/pyrefly-pre-commit
    rev: 1.3.0.dev3 # Note: this is the version of the pre-commit hook, NOT the pyrefly version used for type checking
    hooks:
      - id: pyrefly-check
        name: Pyrefly (type checking)
        pass_filenames: false # Recommended to do full repo checks. However, you can change this to `true` to only check changed files
        language: system # Use system-installed pyrefly
```

# References

[^1]<https://prek.j178.dev/quickstart/#new-to-pre-commit-style-workflows>

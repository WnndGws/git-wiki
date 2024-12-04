---
title: 0001_adding_pre-commit_hook
author: Wynand Gouws
date: 2024-12-04T14:42:07.000Z
public: true
---

## Title: Standardization of pre-commit hooks

### Status: Accepted

## Context

The current development workflow utilizes a custom Git pre-commit hook to execute the `auto_toc.py` script, ensuring the table of contents is updated before each commit. However, this setup lacks flexibility and scalability, particularly when integrating additional tools like TruffleHog for secret detection. To enhance maintainability and extensibility, adopting the `pre-commit` framework is considered.

## Decision

Transition from the custom Git pre-commit hook to the `pre-commit` framework and integrate TruffleHog for secret detection.

### Implementation Steps

0. **Create `.pre-commit-config.yaml`:**

   ```yaml
   repos:
     - repo: local
       hooks:
         - id: auto-toc
           name: Auto TOC Generator
           entry: ./auto_toc.py
           language: python
           stages: [pre-commit]
         - id: trufflehog
           name: TruffleHog
           entry: trufflehog git file://. --since-commit HEAD --no-verification --fail
           language: system
           stages: [pre-commit]
   ```

1. **Install the pre-commit hooks:**

   ```bash
   pre-commit install
   ```

2. **Run hooks against all files:**

   ```bash
   pre-commit run --all-files
   ```

## Consequences

- **Positive:**

  - Streamlined management of pre-commit hooks.
  - Simplified integration of additional tools.
  - Enhanced detection of secrets in the codebase.

- **Negative:**
  - Additional dependencies (`pre-commit` and `trufflehog`).
  - Initial setup time and learning curve.

## References

- [pre-commit Framework](https://pre-commit.com/)
- [TruffleHog GitHub Repository](https://github.com/trufflesecurity/truffleHog)

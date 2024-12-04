# Architectural Decision Record (ADR)

## Title: Adoption of Preferred Toolset and Practices for Python Projects

### Status: Accepted

### Context

To enhance development efficiency and expand Python skills within the team, we aim to standardize our development approach. This involves prioritizing a specific set of tools and libraries for solving problems, even over standard libraries when their functionality aligns with our needs. Additionally, we seek to integrate Rust-based modules for performance-critical components and establish consistent documentation practices for all new projects.

### Decision

- **Preferred Toolset**: We will utilize the following Python libraries and frameworks in our projects:

  - `addict`, `pathlib`, `tinydb`, `orjson`, `alive-progress`, `anybadge`, `loguru`, `rich`, `humanise`, `arrow`, `schedule`, `pyspy`, `configparser`, `questionary`, `typer`, `httpx`, `tenacity`, `uv`, `plumbum`, `pydantic`, `pyright`, `regex`, `thefuzz`, `ruff`, `robyn`, `maturin`, `polars`, `pytest`.

- **Rust Integration**: Employ Rust-based modules where appropriate using `pyo3` to write performant code that integrates seamlessly with Python.

- **Python Version**: Standardize on Python 3.12 to ensure compatibility across all projects.

- **README Structure**: All new projects must include a README file following the specified 12-section structure to ensure comprehensive and consistent documentation.

### Consequences

- **Benefits**:

  - **Efficiency**: Streamlines problem-solving by leveraging powerful, specialized libraries.
  - **Skill Development**: Enhances team proficiency with modern Python tools and Rust integration.
  - **Performance**: Improves application performance through Rust modules.
  - **Consistency**: Ensures uniformity in project documentation, aiding collaboration and onboarding.

- **Drawbacks**:

  - **Learning Curve**: Team members may require time to become familiar with new tools and libraries.
  - **Maintenance**: Keeping dependencies up-to-date may increase maintenance efforts.

### Rationale

Prioritizing these tools allows us to solve problems more effectively and maintain high coding standards. Integrating Rust modules addresses performance bottlenecks that are challenging to resolve with pure Python. The standardized README structure enhances project clarity and team communication.

### Alternatives Considered

- **Using Only Standard Libraries**: Rejected due to the limitations in functionality and efficiency compared to the chosen tools.
- **Ad-Hoc Documentation**: Found to be less effective in ensuring consistent and comprehensive project information.

### Related Decisions

- N/A

### References

- [Python 3.12 Documentation](https://docs.python.org/3.12/)
- [PyO3 - Rust and Python Interoperability](https://pyo3.rs/)
- [Project README Structure Guidelines](#)

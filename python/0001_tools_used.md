## Title: Adoption of Preferred Toolset and Practices for Python Projects

### Status: Accepted

### Context

To enhance development efficiency and expand Python skills within the team, we aim to standardize our development approach. This involves prioritizing a specific set of tools and libraries for solving problems, even over standard libraries when their functionality aligns with our needs. Additionally, we seek to integrate Rust-based modules for performance-critical components and establish consistent documentation practices for all new projects.

### Decision

- **Preferred Toolset**: We will utilize the following Python libraries and frameworks in our projects:

  - `addict`, `pathlib`, `tinydb`, `orjson`, `alive-progress`, `anybadge`, `loguru`, `rich`, `humanise`, `arrow`, `schedule`, `pyspy`, `configparser`, `questionary`, `typer`, `httpx`, `tenacity`, `uv`, `plumbum`, `pydantic`, `pyright`, `regex`, `thefuzz`, `ruff`, `robyn`, `maturin`, `polars`, `pytest`.
  - Here's an overview of each package in your toolkit:
    - **addict**: Provides a dictionary subclass that allows attribute-style access to keys, enabling dot notation for dictionary elements.
    - **alive-progress**: Enables visually appealing and animated progress bars in the terminal, enhancing user experience during long-running processes.
    - **anybadge**: Allows the generation of simple badges in SVG format, useful for displaying build statuses or other metrics.
    - **arrow**: Offers a more intuitive way to work with dates and times in Python, improving upon the standard datetime module.
    - **configparser**: Included in Python's standard library, it provides a way to handle configuration files.
    - **httpx**: A fully featured HTTP client for Python, supporting asynchronous requests and HTTP/2.
    - **humanize**: Adds human-friendly representations of data, such as turning a datetime into a "time ago" string.
    - **loguru**: Simplifies logging in Python with an intuitive syntax and additional features like sink management and message formatting.
    - **maturin**: Facilitates the building and publishing of Rust-based Python packages, streamlining the integration of Rust code into Python projects.
    - **orjson**: A fast JSON library for Python that serializes dataclasses, datetimes, and numpy efficiently.
    - **pathlib**: Offers an object-oriented interface for filesystem paths, simplifying path manipulations and making code more readable.
    - **plumbum**: Offers shell combinators and command-line program integration, facilitating the construction of shell pipelines.
    - **polars**: A fast DataFrame library implemented in Rust, offering efficient data manipulation capabilities.
    - **py-spy**: A sampling profiler for Python programs, useful for identifying performance bottlenecks.
    - **pydantic**: Enforces type annotations at runtime and provides data validation using Python's type hints.
    - **pyright**: A static type checker for Python, designed to be fast and to work with large codebases.
    - **pytest**: A framework that makes it easy to write simple and scalable test cases for Python code.
    - **questionary**: Enables the creation of interactive user prompts in the terminal, enhancing user interaction.
    - **regex**: An alternative to Python's built-in re module, offering extended regular expression support.
    - **rich**: Provides rich text and beautiful formatting in the terminal, including support for tables, progress bars, and syntax highlighting.
    - **robyn**: A high-performance, asynchronous web framework for Python, built with Rust for speed.
    - **ruff**: A fast Python linter, written in Rust, designed to catch common errors and enforce coding standards.
    - **schedule**: Facilitates job scheduling for Python functions, allowing tasks to be run at specific intervals.
    - **tenacity**: Provides retrying behavior for functions, allowing automatic retries with customizable logic.
    - **thefuzz**: Performs fuzzy string matching, useful for finding approximate matches between strings.
    - **tinydb**: A lightweight, document-oriented database written in pure Python, ideal for small projects and applications.
    - **typer**: Simplifies the creation of command-line interfaces, leveraging Python's type hints for automatic argument parsing.
    - **uv**: A Python environment manager that simplifies the management of Python versions and virtual environments.

These tools collectively enhance Python development by providing functionalities ranging from data handling and user interaction to performance profiling and environment management.

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

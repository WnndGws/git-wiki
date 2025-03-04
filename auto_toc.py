#!/usr/bin/env python
"""A script to create my top level toc."""

from pathlib import Path

import regex
from plumbum import local


def generate_readme() -> None:
    """Generate a readme file with a table of contents of subdirectories."""
    current_dir = Path()
    # Get subdirectories, excluding any starting with a dot
    subdirs = [
        d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
    ]

    output_lines = ["# Index\n\n<!--ts-->"]

    for subdir in sorted(subdirs):
        subdir_name = subdir.name.capitalize()
        output_lines.append(f"## {subdir_name}")

        md_files = sorted(subdir.glob("*.md"), key=lambda x: x.name.lower())
        for md_file in md_files:
            md_file_name = md_file.name
            md_file_rel_path = md_file.relative_to(current_dir)
            # Link the file heading to the file
            output_lines.append(f"### [{md_file_name}]({md_file_rel_path})")

            # Extract headings starting with "Title" or "Status"
            with md_file.open("r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    stripped_line = line.strip()
                    if stripped_line.startswith("#"):
                        heading_text = stripped_line.lstrip("#").strip()
                        if heading_text.startswith(("Title", "Status")):
                            # Bold 'Title' or 'Status' at the start
                            heading_text = regex.sub(
                                r"^(Title|Status)", r"**\1**", heading_text
                            )
                            output_lines.append(f"* {heading_text}")

    output_lines.append("\n\n<!--te-->")

    with Path.open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    # Define a shell command
    markdown_toc = local["gh-md-toc"]
    markdown_toc("--insert", "--no-backup", "README.md")


def update_gitattributes() -> None:
    """Update gitattributes to mark markdown files for git-crypt processing."""
    current_dir = Path()
    # Get subdirectories, excluding any starting with a dot
    subdirs = [
        d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
    ]

    for subdir in subdirs:
        # Read the existing .gitattributes file if it exists
        gitattributes_path = subdir / ".gitattributes"
        existing_entries = set()
        if gitattributes_path.exists():
            with gitattributes_path.open("r", encoding="utf-8") as f:
                existing_entries = {line.strip() for line in f if line.strip()}

        # Entries to include in .gitattributes
        entries = set(existing_entries)

        # Get markdown files in the subdirectory
        md_files = list(subdir.glob("*.md"))
        for md_file in md_files:
            with md_file.open("r", encoding="utf-8") as f:
                content = f.read()
                # Extract front matter
                match = regex.match(r"^---\n(.*?)\n---\n", content, regex.DOTALL)
                if match:
                    front_matter = match.group(1)
                    # Check if public: true
                    public_match = regex.search(r"public:\s*(true|false)", front_matter)
                    if public_match:
                        is_public = public_match.group(1).lower() == "true"
                        if is_public:
                            continue  # Skip adding this file to .gitattributes
                # If we get here, we need to add the filename to .gitattributes
                entries.add(f"{md_file.name} filter=git-crypt diff=git-crypt")

        # Write the entries to the .gitattributes file, sorted
        entries = sorted(entries)
        with gitattributes_path.open("w", encoding="utf-8") as f:
            for entry in entries:
                f.write(f"{entry}\n")


if __name__ == "__main__":
    generate_readme()
    update_gitattributes()

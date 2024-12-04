#!/usr/bin/env python
"""A script to create my top level toc."""

from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def generate_readme():
    current_dir = Path()
    # Get subdirectories, excluding any starting with a dot
    subdirs = [
        d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
    ]

    output_lines = ["# Index"]

    for subdir in sorted(subdirs):
        subdir_name = subdir.name.capitalize()
        output_lines.append(f"## {subdir_name}")

        md_files = list(subdir.glob("*.md"))
        for md_file in md_files:
            md_file_name = md_file.name
            md_file_rel_path = md_file.relative_to(current_dir)
            # Link the file heading to the file
            output_lines.append(f"### [{md_file_name}]({md_file_rel_path})")

            # Extract headings starting with "Title" or "Status"
            with md_file.open("r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("#"):
                        heading_text = line.lstrip("#").strip()
                        if heading_text.startswith("Title") or heading_text.startswith(
                            "Status"
                        ):
                            output_lines.append(f"* {heading_text}")

    with open("readme.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))


if __name__ == "__main__":
    app()

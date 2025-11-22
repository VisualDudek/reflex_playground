#!/usr/bin/env python3
"""
Script to traverse the codebase and find all *.md files.
Excludes .venv and other common build/dependency directories.
"""

import os
from pathlib import Path


def find_markdown_files(root_dir: str = ".") -> list[Path]:
    """
    Traverse the directory tree and find all .md files.

    Args:
        root_dir: Root directory to start traversal (default: current directory)

    Returns:
        List of Path objects for all .md files found
    """
    # Directories to exclude from search
    exclude_dirs = {".venv", "venv", "node_modules", "__pycache__", ".git", "dist", "build"}

    markdown_files = []
    root_path = Path(root_dir).resolve()

    for dirpath, dirnames, filenames in os.walk(root_path):
        # Remove excluded directories from traversal
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]

        # Find all .md files in current directory
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = Path(dirpath) / filename
                markdown_files.append(file_path)

    return sorted(markdown_files)


def print_markdown_files(files: list[Path], root_dir: Path):
    """
    Print markdown files with their relative paths.

    Args:
        files: List of Path objects
        root_dir: Root directory for calculating relative paths
    """
    if not files:
        print("No markdown files found.")
        return

    print(f"Found {len(files)} markdown file(s):\n")

    for file_path in files:
        try:
            rel_path = file_path.relative_to(root_dir)
        except ValueError:
            rel_path = file_path

        print(f"  • {rel_path}")


def main():
    """Main entry point."""
    root_dir = Path(__file__).parent

    print(f"Searching for markdown files in: {root_dir}\n")

    md_files = find_markdown_files(root_dir)
    print_markdown_files(md_files, root_dir)


if __name__ == "__main__":
    main()

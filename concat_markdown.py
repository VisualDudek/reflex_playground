#!/usr/bin/env python3
"""
Script to concatenate all markdown files into a single READMEALL.md file.
Uses find_markdown_files from find_markdown.py to locate all .md files.
"""

from pathlib import Path
from find_markdown import find_markdown_files


def concat_markdown_files(output_file: str = "READMEALL.md"):
    """
    Concatenate all markdown files into a single file.

    Args:
        output_file: Name of the output file (default: READMEALL.md)
    """
    root_dir = Path(__file__).parent
    md_files = find_markdown_files(root_dir)

    # Exclude the output file itself if it exists
    output_path = root_dir / output_file
    md_files = [f for f in md_files if f.resolve() != output_path.resolve()]

    if not md_files:
        print("No markdown files found to concatenate.")
        return

    print(f"Found {len(md_files)} markdown file(s) to concatenate.\n")

    with open(output_path, "w", encoding="utf-8") as outfile:
        for i, md_file in enumerate(md_files):
            try:
                rel_path = md_file.relative_to(root_dir)
            except ValueError:
                rel_path = md_file

            print(f"  • Adding: {rel_path}")

            # Write file header with separator
            outfile.write(f"# File: {rel_path}\n\n")
            outfile.write("---\n\n")

            # Read and write file contents
            try:
                with open(md_file, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    outfile.write(content)

                # Add spacing between files (except for last file)
                if i < len(md_files) - 1:
                    outfile.write("\n\n" + "=" * 80 + "\n\n")

            except Exception as e:
                print(f"    Warning: Could not read {rel_path}: {e}")
                outfile.write(f"*Error reading file: {e}*\n\n")

    print(f"\n✓ Concatenated {len(md_files)} file(s) into: {output_file}")


def main():
    """Main entry point."""
    concat_markdown_files()


if __name__ == "__main__":
    main()

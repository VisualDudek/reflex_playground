# Default recipe to display help
default:
    @just --list

# Reflex init
[no-cd]
@init:
    uv run reflex init

# Reflex run
[no-cd]
@run:
    uv run reflex run

# Find markdown files
@findmd:
    uv run find_markdown.py

# Recursive search in mf-files for Takeaway kword
@take:
    grep -r -A 1 -i -n --include="*.md" --color=always "TAKEAWAY" .

# Check for outdated dependencies, dry run
@outdated:
    uv lock --dry-run -U

# Display the dependency tree, depth 1
@dep_tree:
    uv pip tree -d 1
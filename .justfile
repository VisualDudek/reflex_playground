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
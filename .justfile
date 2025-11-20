# Default recipe to display help
default:
    @just --list

# Reflex init
[no-cd]
@init:
    uv run reflex init
# reflex_playground
Learn reflex framework, build web app using pure Python.

- try to use Claude CLI + VS Code extension

## Quick Start
See [GUIDE.md](GUIDE.md) for detailed tutorial.

This project uses [just](https://github.com/casey/just) for task automation.

Common commands:
- `just run` - Run the development server with hot reaload
- `just init` - Initialize a new Reflex app under current dir

# src
[YT Build Full Stack Web Apps in Pure Python with Reflex](https://youtu.be/ITOZkzjtjUA?si=L1_LLilP5YhxL2VU)

# Reflex dependencies
```
reflex v0.8.20
├── alembic v1.17.2
├── click v8.3.1
├── granian v2.6.0
├── httpx v0.28.1
├── packaging v25.0
├── platformdirs v4.5.0
├── pydantic v2.12.4
├── python-multipart v0.0.20
├── python-socketio v5.14.3
├── redis v7.0.1
├── reflex-hosting-cli v0.1.59
├── rich v14.2.0
├── sqlmodel v0.0.27
├── starlette v0.50.0
├── typing-extensions v4.15.0
└── wrapt v2.0.1
watchfiles v1.1.1
└── anyio v4.11.0
```

# Future plans
- Enhance the `find_markdown.py` script

## Python Tips

### Modifying Lists During `os.walk()` Traversal
When using `os.walk()`, the `dirnames` list can be modified in-place to control which directories are visited:

```python
for dirpath, dirnames, filenames in os.walk(root):
    # ✅ Correct: Modifies the actual list os.walk() uses
    dirnames[:] = [d for d in dirnames if d not in exclude_dirs]

    # ❌ Wrong: Creates new list, os.walk() doesn't see changes
    dirnames = [d for d in dirnames if d not in exclude_dirs]
```

The slice assignment `[:]` modifies the **same list object** that `os.walk()` references, allowing you to prune entire directory trees during traversal. This is much more efficient than traversing everything and filtering later.

# gotchas
- The app directory name must start wiht a letter and can contain letters, numbers, and underscores.
- `reflex init --template reflex-chat` 
    - No template know for version 0.8.20
    - Please use `reflex login` to access the `reflex-chat' template
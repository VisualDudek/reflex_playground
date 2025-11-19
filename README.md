# reflex_playground
Learn reflex framework, build web app using pure Python.

- try to use Claude CLI + VS Code extension

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

# gotchas
- The app directory name must start wiht a letter and can contain letters, numbers, and underscores.
- `reflex init --template reflex-chat` 
    - No template know for version 0.8.20
    - Please use `reflex login` to access the `reflex-chat' template
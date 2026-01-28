# Reflex Quick Reference
Last Updated: 2026-01-28

**How to use:** Read top-to-bottom after a break. Keep it under ~200 lines.
**Rule:** If something is not frequently used, it does NOT belong here.

## TOC
- [Install + create project](#install--create-project)
- [Mental model](#mental-model)
- [Essential patterns](#essential-patterns)
- [Review checklist](#review-checklist)

## Install + create project
[CORE]
```bash
uv add reflex
```

## Mental Model (Read First)
[CORE]
- UI is a component tree declared in Python (rx.*)
- State (rx.State) = data + event handlers
- UI reads state vars → events mutate state → UI re-renders
- Distinguish:
    - compile-time (component tree definition)
    - runtime (event handlers, state mutation)

## Minimal App Skeleton
[CORE][STATE][EVENTS]
```python
import reflex as rx

def index() -> rx.Component:
    return rx.text("Hello World")

app = rx.App()
app.add_page(index)
```

## State + Event (Canonical Pattern)
[CORE][STATE][EVENTS]
```python
import reflex as rx

class CounterState(rx.State):
    count: int = 0

    def inc(self):
        self.count += 1

def index() -> rx.Component:
    return rx.vstack(
        rx.heading(CounterState.count),
        rx.button("Increment", on_click=CounterState.inc),
    )

app = rx.App()
app.add_page(index)
```

## Common UI Patterns
[COMMON]
- Conditional rendering: rx.cond(condition, then, else_)
- Lists: render from a state list
- Controlled input:
    - value bound to state
    - update via event handler

## Review Checklist (After Break)
[CORE]
- rx.App() + app.add_page
- How rx.State vars are declared
- How event handlers mutate state
- Controlled input pattern
- Conditional + list rendering
- Dev server still runs (reflex run)

## Links:

# Reflex Code Examples
Last Updated: 2026-01-28

**Purpose:** runnable snippets + muscle memory.

---

## Hello World
[CORE]

```python
import reflex as rx

def index() -> rx.Component:
    return rx.text("Hello World")

app = rx.App()
app.add_page(index)
```

## Counter (State + Event)
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

## Controlled Input
[COMMON][STATE]
```python
import reflex as rx

class FormState(rx.State):
    name: str = ""

    def set_name(self, value: str):
        self.name = value

def index():
    return rx.vstack(
        rx.input(value=FormState.name, on_change=FormState.set_name),
        rx.text(FormState.name),
    )

app = rx.App()
app.add_page(index)
```

## Conditional Rendering
[COMMON]
```python
rx.cond(
    CounterState.count > 5,
    rx.text("High"),
    rx.text("Low"),
)
```
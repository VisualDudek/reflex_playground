# Full Width Navbar and Content

- use `rx.fragment()` Component for no CSS, no id ???(id on box shows diffrent), no any styles -> useful to 
- drop `rx.container()` in `base_layout()` in favour to `rx.fragment()` and style individual components -> full width navbar
- `.vstack()` -> Layout -> check in docs `align` and `justify` for this Component

## Tip with return huge code block
You can always refactor this:
```python
def index() -> rx.Component:
    return base_layout(
        rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
```
into this:
```python
def index() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Welcome to Reflex!", size="9"),
        ...,
    )
    return base_layout(my_child,)
```

# Pages and URL Routes
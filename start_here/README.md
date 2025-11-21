# Step by step for "start here"

## Color mode
-`rx.color_mode.button(position="top-right")`
- play with position

## Buttons
- `rx.button("Check out our docs!")`
- add new button
- have `on_click` kwarg that is Event type
- add `State` method as event to button `on_click`

## App state
- This is huge thing
- subclass of `rx.State`
- can keep state in class attribute
- via adding methods to this subclass you can dynamic do things, e.g. change label
- add method that change label attribute
- use `itertools.cycle` for smart toggle_label method

## Text
- Does `rx.text` also have `on_click`? YES
- try `on_click` on `rx.text`

# Questions
- what are `.web` and `.state` dirs?
- `on_click` is Button kwarg but plays Event role?

# Takeaway

### Tracing Component Base Classes (e.g., `rx.text`)

Your IDE shows `rx.text` as `TextNamespace`, not the actual component class. Here's how to find the real inheritance:

1. **`rx.text` is a `ComponentNamespace` instance**, not a class
2. Look for `__call__` in the namespace - it points to the actual component's `.create()` method:
   ```python
   class TextNamespace(ComponentNamespace):
       __call__ = staticmethod(Text.create)  # <-- rx.text() calls this
   ```
3. The `Text` class has the real inheritance chain:
   ```
   Component → Element → BaseHTML → Span → Text
   ```

### How Event Handlers (`on_click`, etc.) Work

Event handlers like `on_click` are **not** inherited through class attributes. Instead:

1. A module-level `DEFAULT_TRIGGERS` dict defines common events for all components:
   ```python
   DEFAULT_TRIGGERS = {
       EventTriggers.ON_CLICK: pointer_event_spec,
       EventTriggers.ON_FOCUS: no_args_event_spec,
       # ...
   }
   ```
2. `Component.get_event_triggers()` merges these defaults with component-specific triggers:
   ```python
   return DEFAULT_TRIGGERS | args_specs_from_fields(cls.get_fields())
   ```

This is why every component automatically supports `on_click`, `on_focus`, `on_blur`, etc.
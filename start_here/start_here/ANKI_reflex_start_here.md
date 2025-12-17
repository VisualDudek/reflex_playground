# Reflex Anki Cards (from `start_here.py`)

These cards are based on the Reflex concepts used in `start_here/start_here/start_here.py`.

## Import into Anki (TSV)

- In Anki: **File → Import**
- Set **Field separator** to **Tab**
- Map fields: **Front** = Field 1, **Back** = Field 2

Copy-paste the following into a `.tsv` file (or import directly from clipboard if your workflow supports it):

```tsv
State: What do you inherit from to define app state in Reflex?	rx.State
State: How do you declare a reactive state variable?	As a typed class attribute on the rx.State class (e.g., label: str = "...").
State: In a State method, how do you update reactive state?	Assign to self.<var> (e.g., self.label = "...").
State: In a component, how do you read a state variable?	Use State.<var> (e.g., State.label).
State: What’s the purpose of a leading-underscore attribute like _label_cycle in State?	It’s an internal/private attribute (not meant for UI binding); keep non-UI Python objects there.
Events: How do you connect a UI event to a State method in Reflex?	Pass the method reference to an event prop (e.g., on_click=State.change_label).
Events: When assigning on_click=State.some_method, do you include parentheses?	No—pass the function reference, not a call.
Events: What happens conceptually when a button triggers State.change_label?	The event runs the State method; updating self.label causes dependent UI to re-render.
UI: What does rx.container(...) typically provide?	A layout wrapper (often centered content + consistent padding/margins).
UI: What does rx.vstack(...) do?	Stacks children vertically (column layout) with spacing/align options.
UI: How do you display a heading in Reflex?	rx.heading("text", size="...")
UI: How do you display dynamic text from state as a heading?	Use the state var where text goes (e.g., rx.heading(State.label, ...)).
UI: How do you render inline code-style text?	rx.code("...")
UI: How do you build mixed text + inline code in one line?	Use rx.text("prefix ", rx.code("..."), ...).
UI: Which component in the file creates a color-mode toggle button?	rx.color_mode.button(...)
UI: How do you position the color-mode button in this example?	Pass position="top-right".
UI: How do you create a button in Reflex?	rx.button("Label", on_click=...)
UI: How do you make a link open in a new tab/external context?	Use rx.link(..., href="...", is_external=True).
UI: In this example, how is a button turned into a link?	Wrap rx.button(...) inside rx.link(...).
Pages: What is the page function called in this file?	index
Pages: What does def index() -> rx.Component: indicate?	The page function returns a Reflex component tree.
App: How do you create the app instance?	app = rx.App()
App: How do you register a page with the app?	app.add_page(index)
Config: How does the UI get the app name for display?	From rxconfig import config, then config.app_name.
Python: What standard-library tool is used to alternate label values?	itertools.cycle
Python: How does toggle_label alternate values without if/else?	It sets self.label = next(self._label_cycle).
```

## Readable version (Markdown table)

| Front | Back |
|---|---|
| State: What do you inherit from to define app state in Reflex? | `rx.State` |
| State: How do you declare a reactive state variable? | As a typed class attribute on the `rx.State` class (e.g., `label: str = "..."`). |
| State: In a State method, how do you update reactive state? | Assign to `self.<var>` (e.g., `self.label = "..."`). |
| State: In a component, how do you read a state variable? | Use `State.<var>` (e.g., `State.label`). |
| State: What’s the purpose of a leading-underscore attribute like `_label_cycle` in State? | It’s an internal/private attribute (not meant for UI binding); keep non-UI Python objects there. |
| Events: How do you connect a UI event to a State method in Reflex? | Pass the method reference to an event prop (e.g., `on_click=State.change_label`). |
| Events: When assigning `on_click=State.some_method`, do you include parentheses? | No—pass the function reference, not a call. |
| Events: What happens conceptually when a button triggers `State.change_label`? | The event runs the State method; updating `self.label` causes dependent UI to re-render. |
| UI: What does `rx.container(...)` typically provide? | A layout wrapper (often centered content + consistent padding/margins). |
| UI: What does `rx.vstack(...)` do? | Stacks children vertically (column layout) with spacing/align options. |
| UI: How do you display a heading in Reflex? | `rx.heading("text", size="...")` |
| UI: How do you display dynamic text from state as a heading? | Use the state var where text goes (e.g., `rx.heading(State.label, ...)`). |
| UI: How do you render inline code-style text? | `rx.code("...")` |
| UI: How do you build mixed text + inline code in one line? | Use `rx.text("prefix ", rx.code("..."), ...)`. |
| UI: Which component in the file creates a color-mode toggle button? | `rx.color_mode.button(...)` |
| UI: How do you position the color-mode button in this example? | Pass `position="top-right"`. |
| UI: How do you create a button in Reflex? | `rx.button("Label", on_click=...)` |
| UI: How do you make a link open in a new tab/external context? | Use `rx.link(..., href="...", is_external=True)`. |
| UI: In this example, how is a button turned into a link? | Wrap `rx.button(...)` inside `rx.link(...)`. |
| Pages: What is the page function called in this file? | `index` |
| Pages: What does `def index() -> rx.Component:` indicate? | The page function returns a Reflex component tree. |
| App: How do you create the app instance? | `app = rx.App()` |
| App: How do you register a page with the app? | `app.add_page(index)` |
| Config: How does the UI get the app name for display? | From `rxconfig import config`, then `config.app_name`. |
| Python: What standard-library tool is used to alternate label values? | `itertools.cycle` |
| Python: How does `toggle_label` alternate values without if/else? | It sets `self.label = next(self._label_cycle)`. |

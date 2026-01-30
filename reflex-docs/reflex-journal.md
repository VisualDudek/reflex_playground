# Reflex Learning Journal
Last Updated: 2026-01-30

**Purpose:** chronological learning log.  
**Rule:** Raw notes go here first; distilled knowledge moves elsewhere.

---

## 2026-01-28 — Session 1
**Focus:** setup + first app

### What I did
- Installed Reflex
- Ran `reflex init` and `reflex run`

### What I learned
- `import reflex as rx` is standard
- App requires `rx.App()` and `app.add_page(index)`

### Friction / Errors
- (none yet)

### Next Session
- State + event handler (counter)
- Controlled input example

Links:
- Quick ref → `./reflex-quick-ref.md`
- Examples → `./reflex-examples.md#hello-world`
- Concepts → `./reflex-concepts.md#foundations`

## 2026-01-30 — Session 2
**Focus:** recap

### What I did
- recap [start here app](../start_here/)
- dig into how components are created and exposed in `rx` module

### Questions
- why rx module expose Container.create classmethod in such way `container = Container.create`?

### What I learned
- `rxconfig.py` defines app name (implicit app dir) and plugins such as `tailwind` and `Sitemap`
- [CONCEPT:Prop] Props modify the behavior and appearance of components. They are passed in as keyword arguments to a component.
- [COMPONENT/STYLE] page dark mode toggle button is Component `rx.color_mode.button(position="top-right")`
- [COMPONENT/EVENT] both `rx.button` and `rx.text` support `on_click` prop that takes an Event handler (usually a State method) type: `EventType`.
- [COMPONENT] `rx.text`, `rx.button`, `rx.link`, `rx.heading`
- [COMPONENT:LAYOUT] `rx.vstack`, `rx.hstack`, `rx.box`
- [STATE] class that inherits from `rx.State` holds app state **variables** as class attributes and event handler methods that mutate those variables. [Counter example](./reflex-examples.md#counter-state--event)

### Friction / Errors
- (none yet)

### Next Session
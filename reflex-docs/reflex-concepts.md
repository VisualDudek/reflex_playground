# Reflex Concepts
Last Updated: 2026-01-28

**Purpose:** conceptual map for fast recall and deep understanding.

---

## Foundations
### App Structure
[CORE]

- `app = rx.App()`
- `app.add_page(fn)` registers a page

**Why it matters:** routing and page composition are the backbone.

See: `./reflex-examples.md#hello-world`

### Components
[CORE]

- UI is a nested tree of `rx.*` components
- Layout is explicit (e.g. `rx.vstack`, `rx.hstack`)
- Different types of components such as Layout, Forms, Data Display [see here](https://reflex.dev/docs/library/)

### Props
[CORE]
- Modify component behavior/appearance [See: Styling section below](#styling)
- Passed as keyword args (e.g. `rx.button("Click me", color="red")`)

## State & Events
### State (`rx.State`)
[CORE][STATE]

- Holds reactive variables
- Declares event handlers
- UI reads state directly (`State.var`)

### Event Handlers
[CORE][EVENTS]

- Triggered by UI events (`on_click`, `on_change`)
- Must mutate state vars
- Drive all dynamic behavior

## Rendering Patterns
### Conditional Rendering
[COMMON]

- Use `rx.cond`
- Avoid Python `if` inside component trees

### List Rendering
[COMMON]

- Iterate over state lists
- Each item maps to a component

## Styling
[COMMON]

- Style via component props
- Prefer composable layout over CSS-first thinking

## Deployment (Placeholder)
[ADVANCED]

- Add notes here when first deploying

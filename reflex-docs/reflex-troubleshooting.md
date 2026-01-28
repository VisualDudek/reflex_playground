# Reflex Troubleshooting
Last Updated: 2026-01-28

**Purpose:** reduce future debugging time.

---

## State Updates Not Reflected
[COMMON][STATE]

**Symptom:** UI doesn’t change after mutation

**Causes**
- Mutating non-state variable
- Handler not wired to component

**Fix**
- Ensure var is declared on `rx.State`
- Ensure handler mutates `self.var`


## Event Handler Not Firing
[COMMON][EVENTS]

**Symptom:** button click does nothing

**Fix checklist**
- `on_click=State.handler`
- Handler signature matches event


## App Won’t Start
[COMMON]

**Checklist**
- Virtualenv activated
- `pip install reflex`
- Run from project root

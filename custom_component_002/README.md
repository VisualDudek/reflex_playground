# Building a Custom Reflex Component

Mind setup: 
- see "Why Create Custom Container Components" 
- components are made up of children and props.
- you can incorporate simple/comlex conditions what and how show e.g. based on arg: `hide_navbar` or
- **TAKEAWAY** based on type!!! `isinstance()`
<!-- TAG: TODO -->
- **FUTURE PLANS** ^^^ good palace to use structural matching patterns?

## rx.container deep dive
- try to replace `rx.container()` inside `index()` with custom fn.
- **TAKEAWAY** that type of obj. custom container should takes in?
```python
def base_page(*args, **kwargs) -> rx.Component:
    print([type(arg) for arg in args])
    return rx.container()
```
```txt
[<class 'reflex.components.radix.themes.components.icon_button.IconButton'>, <class 'reflex.components.radix.themes.layout.stack.VStack'>]
```

## Why Create Custom Container Components?

By creating a custom wrapper function (like `base_page`), you can **abstract away repetitive elements** that appear on every page:

```python
def base_page(*args, **kwargs) -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),  # Same on every page
        navbar(),  # Same on every page
        *args,     # Page-specific content
    )
```

**Benefits:**
- **DRY principle** - Define navbar, footer, dark mode button once
- **Consistency** - All pages have the same layout structure
- **Easy updates** - Change one place, affects all pages

Then each page just passes its unique content:
```python
def index() -> rx.Component:
    return base_page(
        rx.heading("Home"),
        # ... page-specific content only
    )

def about() -> rx.Component:
    return base_page(
        rx.heading("About"),
        # ... page-specific content only
    )
```
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

- now adding new pages is easy, just copy `index()` and add routing
```python
app.add_page(about_page, route='/about')`
```
- and edit link in navbar
- keep project structure:
    - `/ui`
    - `/pages`

TAKEAWAY: instead of importing each new page from module
```python
from .pages.about import about_page
from .pages.index import index
```
make `/pages` a package -> add `__init__.py` with dunder `__all__`
```python
from .about import about_page
from .index import index

__all__ = [
    "about_page", 
    "index",
    ]
```
than you can:
```python
from . import pages
```
and
```python
app.add_page(pages.index)
app.add_page(pages.about_page, route="/about")
```

# USing Link-based Navigation

- using `rx.link()` make logo to point into home page
- use `navbar_link` inside `navbar_buttons()` to create href
- it won't work for `rx.mobile_and_tablet()`

# Click Events and Reflex Redirect

Takeaway: mindsetup -> insted of link use event on_click + `rx.redirect()` (programmatic approach)

BUT programmatic approach wont give you e.g. copy url link on Button so in those simple usage stick to button inside link

- use decorator `rx.page(route='')` to register pages instead of `app.add_page(pages.about_page, route="/about")`

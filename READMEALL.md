# File: GUIDE.md

---

# Guide

Mind setup:
- you are building your frontent using Components what are renderd out to HTML

## Creating a New Reflex App

### Basic Initialization

To create a new Reflex app:
```bash
uv run reflex init
# or use justfile
just init
```

**Important:** `reflex init` creates a subdirectory with your app name and generates the main configuration file `rxconfig.py` in the current directory. The structure will look like:

```
current_directory/
    rxconfig.py          # Main Reflex configuration file
     myapp/               # App directory (subdirectory with the app name)
         __init__.py
        myapp.py        # Your main app code
    assets/             # Static assets (created automatically)
```

**Note:** Some templates require authentication. Use `just login` first if you get a template access error.

### App Naming Rules

From the Reflex documentation:
- The app directory name must start with a letter
- Can contain letters, numbers, and underscores only
- No spaces or special characters

## Running Your App

Run the development server with **hot reload**:
```bash
just run
```

This starts both frontend and backend servers. The app will be available at `http://localhost:3000` by default.

### Copying Existing Projects

When copying an old project into a newly initialized Reflex app, **delete all `*.pyc` files** to avoid potential conflicts:

```bash
find . -name "*.pyc" -delete
```

This removes cached Python bytecode files that may cause issues with the new environment.

## Built-in Features

**Light/Dark Mode:** Reflex apps come with light/dark mode support out of the box. No additional configuration required.

## Project Configuration Files

- `rxconfig.py` - Reflex app configuration (created after `reflex init`)


================================================================================

# File: README.md

---

# reflex_playground
Learn reflex framework, build web app using pure Python.

- try to use Claude CLI + VS Code extension

## Quick Start
See [GUIDE.md](GUIDE.md) for detailed tutorial.

This project uses [just](https://github.com/casey/just) for task automation.

Common commands:
- `just run` - Run the development server with hot reaload
- `just init` - Initialize a new Reflex app under current dir

# src
[YT Build Full Stack Web Apps in Pure Python with Reflex](https://youtu.be/ITOZkzjtjUA?si=L1_LLilP5YhxL2VU)

# Reflex dependencies
```
reflex v0.8.20
├── alembic v1.17.2
├── click v8.3.1
├── granian v2.6.0
├── httpx v0.28.1
├── packaging v25.0
├── platformdirs v4.5.0
├── pydantic v2.12.4
├── python-multipart v0.0.20
├── python-socketio v5.14.3
├── redis v7.0.1
├── reflex-hosting-cli v0.1.59
├── rich v14.2.0
├── sqlmodel v0.0.27
├── starlette v0.50.0
├── typing-extensions v4.15.0
└── wrapt v2.0.1
watchfiles v1.1.1
└── anyio v4.11.0
```

# Future plans
- Enhance the `find_markdown.py` script
- Use Markdown comment syntax `<!-- TAG: TAKEAWAY --->` for takaway points
- ^^^ follow up, script that walk all .md files and gather TAKEAWAY tags

## Debug
For `rx.page()` decorator, there is this key line:
```python
        DECORATED_PAGES[get_config().app_name].append((render_fn, kwargs))
```
how to debug this dict DECORATED_PAGES?

## Python Tips

### Modifying Lists During `os.walk()` Traversal
When using `os.walk()`, the `dirnames` list can be modified in-place to control which directories are visited:

```python
for dirpath, dirnames, filenames in os.walk(root):
    # ✅ Correct: Modifies the actual list os.walk() uses
    dirnames[:] = [d for d in dirnames if d not in exclude_dirs]

    # ❌ Wrong: Creates new list, os.walk() doesn't see changes
    dirnames = [d for d in dirnames if d not in exclude_dirs]
```

The slice assignment `[:]` modifies the **same list object** that `os.walk()` references, allowing you to prune entire directory trees during traversal. This is much more efficient than traversing everything and filtering later.

# gotchas
- The app directory name must start wiht a letter and can contain letters, numbers, and underscores.
- `reflex init --template reflex-chat` 
    - No template know for version 0.8.20
    - Please use `reflex login` to access the `reflex-chat' template
- `ImportError: cannot import name 'State' from partially initialized module 'part_006.part_006' (most likely due to a circular import)`

# Takeaway
vim-mode when using fold on code block: Use `gj` and `gk` instead of `j` and `k`
They move visually, not logically — this does not enter folds, so they stay closed.

Jump to next / previous paragraph: Use `{` and `}`. A paragraph is separated by blank lines.

================================================================================

# File: code_management_004/README.md

---

# Better Code Management

When building Reflex apps, keep your code organized by splitting it into separate files.

- add navbar recipe
- add base_layout
- Break code into smaller files. `./ui`:
    - `navbar.py`
    - `base_page.py`
    - use "Relative import" `from . import module_name`


================================================================================

# File: custom_component_002/README.md

---

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
- you can validate if all args are `rx.Component`

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

================================================================================

# File: html_input_001/README.md

---

# html input for dynamic input

- event vs. event handlers, the first one is on frontend/user UI space and the "event hadlers" refers to backend

## Props
- there is also `on_change` event, will be called on every change e.g. single chr

## Input
- `rx.input()` works with `on_change` props
- can have `placeholder` or `default_value`

================================================================================

# File: id_rendered_comp_005/README.md

---

# Identifying Rendered Components in the Browser

- add `id="str"` kward to rx component and next inspect web page
- try to find kwarg that act as parameter (on given rx.component) and find according docs e.g. 
```python
rx.vstack(
    ...
    spacing="5",
    justify="center",
    min_height="85vh",
)
```

================================================================================

# File: navbar_recipe_003/README.md

---

# Using the Navbar Recipe

## src
- [Reflex Navigation Bar](https://reflex.dev/docs/recipes/layout/navbar#navigation-bar)

## Navbar Recipe
- add recipe
- create `base_layout()` wraper that will have permament Navbar
- add `logo.jpg` into assetes
- `rx.desktop_only()` and `rx.mobile_and_tablet()` for proper rendering depending on device.

================================================================================

# File: part_006/README.md

---

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

# URL Route Path Constatnts
solving typos issues in hardcoded url redirections in many places, "one source of truth"

- create navigation package `/navigation/routes.py`
- use on above package same trick with `__all__` dunder 

# Navigation State
solving on_click event redirect State usecase: mobile navbar -> `rx.menu.item("About")`

- create `/navigation/state.py`
- add redirext methods to `NavState` class
- edit `__init__` for navigation pkg in order to make  


================================================================================

# File: part_007/part_007/README.md

---

# Contact Form

- add contact page:
    - use decorator to register url
    - do not forget to add to pkg, ~~when decorator is used it seems not needed BUT for sanity~~ Takeaway: why it is not working when decorator is used and not included into pkg?
    - use `navigation routes`
    - do not forget add links in navbar
- use docs form recipe
    - add `tx.text_area`
    - make name required
    - add email with type email, default is text

# Making the From Responsive (styling)
- styling with common Inline Styles
- use `rx.desktop_only()` for rendering Components only in desktop mode
- use `rx.box()` Component for styling
- Takeaway: 50vw stands for 50% "viewport width" -> 50% of the browser windows's width
- make name and last name in same row

# Conditional Rendering in Reflex
getting familiar with:
- `rx.cond()` keep in mind that both Components need to be the same type
- `@rx.var` Takeaway: rx is using `@overload` for this decorator

- use FormState to keep bool for rx.cond
- challenge with clearing thank_you_message rendered by `rx.cond`
    - timeout approach 

# Refresh State with Python Asyncio Timeouts
Takeaway: using `yield` for async method for refreshing state?

- kind of magic:
```python
        yield
        await asyncio.sleep(2) 
        self.did_submit = False
        yield
```

# Counting with Asyncio and Reflex
how to start async countdown fn.? -> use `on_load` for `rx.page()` 

- add rx.var time_left inside ContactFormState class
- add async countdown
- start countdown async fn. on load

================================================================================

# File: part_database_008/README.md

---

# Your First Database Model
get familiar with: 
- docs-> Learn / State / Database
- ORM

Reflex uses SQLModel to provide a built-in ORM wrapping SQLAlchemy.

Reflex leverages `alembic` to manage db schema changes.

There is `alembic.ini` config file

- add db_url into `rxconfig.py`
- create ContactEntryModel subclass of `rx.Model`
- init db `reflex db init`
- makemigrations
- migrate
- check `alembic/script.py.mako`
- you need to explicite `table=True` for models make effect in SQL
- now `just dbmakeall` will make reference point

# Storing Date with Models and Forms


================================================================================

# File: start_here/README.md

---

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

## Props
- Attributes that affect the behavior and appearance of component.
- React naming convention for component inputs (properties). Reflex uses it because the Python code compiles to React components.
```python
# component.py:1032
@classmethod
def create(cls: type[T], *children, **props) -> T:
    # props = {"on_click": State.do_something}
```
- `_post_init()` processes the props:
```python
# component.py:744-747
fields = self.get_fields() # Class field definitions (Var types)
component_specific_triggers = self.get_event_triggers()  # {"on_click": pointer_event_spec, ...}
props = self.get_props() # Valid prop names for this component
```

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
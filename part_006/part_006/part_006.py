"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .pages.about import about_page
from .ui.base_layout import base_layout


class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Welcome to Reflex!", size="9"),
        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),
        rx.input(
            placeholder="Type something...",
        ),
        rx.link(
            rx.button("Check out our docs!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="welcome-vstack",
    )
    return base_layout(my_child,)


app = rx.App()
app.add_page(index)
app.add_page(about_page, route="/about")
"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .pages.about import about_page
from .pages.index import index
from .ui.base_layout import base_layout


class State(rx.State):
    """The app state."""

app = rx.App()
app.add_page(index)
app.add_page(about_page, route="/about")
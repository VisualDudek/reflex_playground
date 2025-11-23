"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import pages


class State(rx.State):
    """The app state."""

app = rx.App()
app.add_page(pages.index)
app.add_page(pages.about_page, route="/about")
"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import pages


class State(rx.State):
    """The app state."""

    def redirect_to_about(self):
        """Redirect to the about page."""
        return rx.redirect("/about")

app = rx.App()
app.add_page(pages.index)
# app.add_page(pages.about_page, route="/about")
# insead of the above line, use decorator on the about_page function
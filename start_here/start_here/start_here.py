"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from itertools import cycle


class State(rx.State):
    """The app state."""
    label: str = "Hello, Reflex!"
    _label_cycle = cycle(["Hello, Reflex!", "You clicked the button!"])

    def change_label(self):
        """Change the label."""
        self.label = "You clicked the button!"

    def toggle_label(self):
        """Toggle the label between two states."""
        self.label = next(self._label_cycle)


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.button(
                "Click me!",
                on_click=State.change_label,
            ),
            rx.button(
                "Toggle Label",
                on_click=State.toggle_label,
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)

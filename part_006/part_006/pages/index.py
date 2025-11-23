import reflex as rx
from rxconfig import config
from ..ui.base_layout import base_layout

class State(rx.State):

    def redirect_to_about(self):
        """Redirect to the about page."""
        return rx.redirect("/about")
    

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
        rx.button("Event with redirect", on_click=State.redirect_to_about),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="welcome-vstack",
    )
    return base_layout(my_child,)


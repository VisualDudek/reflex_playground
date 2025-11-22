import reflex as rx
from .navbar import navbar_buttons

def base_layout(*children: rx.Component) -> rx.Component:
    """The base layout for the app."""
    return rx.container(
        navbar_buttons(),
        *children,
        padding="1rem",
        max_width="800px",
        margin="0 auto",
    )


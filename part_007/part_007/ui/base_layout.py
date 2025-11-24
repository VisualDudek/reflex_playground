import reflex as rx
from .navbar import navbar_buttons


def base_layout(*children: rx.Component) -> rx.Component:
    return rx.fragment(
        navbar_buttons(),
        rx.color_mode.button(position="bottom-left"),
        rx.box(
            *children,
            id="my-content-box",
            padding="1em",
            width="100%",
        ),
    )


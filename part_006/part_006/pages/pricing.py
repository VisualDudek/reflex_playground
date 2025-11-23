import reflex as rx
from ..ui.base_layout import base_layout


def pricing_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Pricing Page", size="9"),
        rx.text(
            "Pricing information about this app. Edit ",
            size="5",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="welcome-vstack",
    )
    return base_layout(my_child,)


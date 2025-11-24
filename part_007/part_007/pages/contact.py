import reflex as rx
from ..ui.base_layout import base_layout
from ..navigation import routes


class ContactFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print("Form submitted:", form_data) # For debugging
        self.form_data = form_data


@rx.page(route=routes.CONTACT_ROUTE)  # route decorator alternative to app.add_page
def contact_page() -> rx.Component:
    my_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    placeholder="First Name", 
                    name="first_name", 
                    required=True,
                    width="100%",
                ),
                rx.input(
                    placeholder="Last Name", 
                    name="last_name",
                    width="100%",
                ),
                spacing="3",
                width="100%",
            ),
            rx.input(
                name="email", 
                placeholder="Email", 
                type="email",
                width="100%",
            ),
            rx.text_area(
                placeholder="Your Message", 
                name="message",
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=ContactFormState.handle_submit,
        reset_on_submit=True,
    ),
    my_child = rx.vstack(
        rx.heading("Contact Page", size="9"),
        rx.desktop_only(
            rx.box(
                my_form,
                width="50vw",
            ),
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="welcome-vstack",
    )
    return base_layout(my_child,)


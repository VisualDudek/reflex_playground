import reflex as rx
import asyncio
from ..ui.base_layout import base_layout
from ..navigation import routes


class ContactFormState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    time_left: int = 5

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print("Form submitted:", form_data) # For debugging
        self.form_data = form_data
        self.did_submit = True
        yield
        await asyncio.sleep(2) 
        self.did_submit = False
        yield
    
    @rx.var
    def thank_you_message(self) -> str:
        return f"Thank you, {self.form_data.get('first_name', 'Guest')}! We have received your message."
    
    @rx.var
    def time_left_label(self) -> str:
        if self.time_left < 1:
            return "Time's up!"
        return f"Left: {self.time_left} seconds"
    
    async def countdown(self):
        while self.time_left > 0:
            await asyncio.sleep(1)
            self.time_left -= 1
            yield


@rx.page(
        on_load=ContactFormState.countdown,
        route=routes.CONTACT_ROUTE,
)  # route decorator alternative to app.add_page
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
        rx.text(
            ContactFormState.time_left_label,
        ),
        rx.cond(
            ContactFormState.did_submit, 
            rx.text(ContactFormState.thank_you_message), 
            None),  # Placeholder for submission confirmation
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


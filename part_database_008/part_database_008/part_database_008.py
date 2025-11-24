import reflex as rx

from . import pages, navigation


class State(rx.State):
    """The app state."""

    def redirect_to_about(self):
        """Redirect to the about page."""
        return rx.redirect("/about")

app = rx.App()
app.add_page(pages.index, route=navigation.routes.HOME_ROUTE)
# app.add_page(pages.about_page, route="/about")
# instead of the above line, use decorator on the about_page function
app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)
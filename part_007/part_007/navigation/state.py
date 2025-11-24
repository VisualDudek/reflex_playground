import reflex as rx
from . import routes

class NavState(rx.State):
    """The navigation state."""

    def to_home(self):
        """Navigate to the home page."""
        return rx.redirect(routes.HOME_ROUTE)
    

    def to_about(self):
        """Navigate to the about page."""
        return rx.redirect(routes.ABOUT_ROUTE)
    

    def to_pricing(self):
        """Navigate to the pricing page."""
        return rx.redirect(routes.PRICING_ROUTE)
    

    

    

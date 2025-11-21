import reflex as rx

config = rx.Config(
    app_name="navbar_recipe_003",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
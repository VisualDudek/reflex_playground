import reflex as rx

config = rx.Config(
    app_name="start_here",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
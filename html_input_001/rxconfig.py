import reflex as rx

config = rx.Config(
    app_name="html_input_001",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
import reflex as rx

config = rx.Config(
    app_name="custom_component_002",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
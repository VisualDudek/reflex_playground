import reflex as rx

config = rx.Config(
    app_name="part_006",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
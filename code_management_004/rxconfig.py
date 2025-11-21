import reflex as rx

config = rx.Config(
    app_name="code_management_004",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
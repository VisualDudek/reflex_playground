import reflex as rx

config = rx.Config(
    app_name="part_database_008",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    db_url="sqlite:///part_database_008.db",
)
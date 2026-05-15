import reflex as rx

config = rx.Config(
    app_name="qualitec_vitrine",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
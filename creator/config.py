from .modules import rust, python, vite, astro

APP_NAME = "creator"
LANGUAGES = {
    "rust": rust.run,
    "python": python.run,
    "vite": vite.run,
    "astro": astro.run
}

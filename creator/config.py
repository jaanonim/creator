from .modules import rust, python, vite

APP_NAME = "creator"
LANGUAGES = {
    "rust": rust.run,
    "python": python.run,
    "vite": vite.run,
}

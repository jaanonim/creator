from .modules import astro, python, rust, sveltekit, vite

APP_NAME = "creator"
LANGUAGES = {
    "rust": rust.run,
    "python": python.run,
    "vite": vite.run,
    "astro": astro.run,
    "sveltekit": sveltekit.run,
}

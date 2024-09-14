import enum
from .modules import astro, python, rust, sveltekit, vite
from .runners import default, nix

APP_NAME = "creator"
_LANGUAGES = {
    "rust": rust,
    "python": python,
    "vite": vite,
    "astro": astro,
    "sveltekit": sveltekit,
}

_RUNNERS = {
    "default": default.CLASS,
    "nix": nix.CLASS,
}


LANGUAGE = enum.Enum('Language', dict([
    (k, k) for k in _LANGUAGES
]))

RUNNER = enum.Enum('Runner', dict([
    (k, k) for k in _RUNNERS
]))

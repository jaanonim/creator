import os
from pathlib import Path

import questionary

from ..util import run_command


def run(path: Path, name: str):
    os.chdir(path)
    os.system(f"pnpm create vite@latest {name}")
    project_path = path / name
    os.chdir(project_path)

    if questionary.confirm(f"To what to install dependencies?").ask():
        run_command("Installing dependencies...", "pnpm", "i")

    return False, project_path

import os
from pathlib import Path
import questionary

from ..util import run_command


def run(path: Path, name: str):
    os.chdir(path)
    os.system(f"npm create vite@latest {name}")
    project_path = path / name
    os.chdir(project_path)

    if questionary.confirm(f"To what to install dependencies?").ask():
        run_command("Installing dependencies...", "npm", "i")

    return project_path

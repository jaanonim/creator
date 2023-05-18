import os
from pathlib import Path

from ..util import run_command


def run(path: Path, name: str):
    project_path = path / name
    project_path.mkdir(parents=True, exist_ok=True)
    os.chdir(project_path)
    run_command("Creating project...", "cargo", "init")

    f = open(project_path / "README.md", "w")
    f.write(f"# {name}\n")
    f.close()

    return project_path

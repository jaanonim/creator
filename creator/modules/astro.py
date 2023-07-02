import os
from pathlib import Path


def run(path: Path, name: str):
    os.chdir(path)
    os.system(f"pnpm create astro@latest {name}")
    project_path = path / name
    os.chdir(project_path)

    return True, project_path

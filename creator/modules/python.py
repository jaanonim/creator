import os
from pathlib import Path

from ..util import run_command


def run(path: Path, name: str):
    project_path = path / name
    project_path.mkdir(parents=True, exist_ok=True)
    os.chdir(project_path)

    f = open(project_path / "main.py", "w")
    f.write('\ndef main():\n\tpass\n\n\nif __name__ == "__main__":\n\tmain()\n')
    f.close()

    f = open(project_path / ".gitignore", "w")
    f.write("env\n.vscode\n__pycache__\n.idea\n")
    f.close()

    f = open(project_path / "README.md", "w")
    f.write(f"# {name}\n")
    f.close()

    f = open(project_path / "requirements.txt", "w")
    f.write(f"")
    f.close()

    run_command("Creating env...", "python3", "-m", "venv", "env")
    return False, project_path

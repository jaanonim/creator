import os
from pathlib import Path

import questionary

from ..command import run_command


class Default:
    def __init__(self, language, path: Path, name: str):
        self.path = path
        self.name = name
        self.language = language
        self.project_path = path.joinpath(name)

    def run_command_interactive(self, cmd: str, use_project_path=True):
        os.chdir(self.project_path if use_project_path else self.path)
        os.system(" ".join(self.get_cmd(cmd)))

    def run_command(self, description: str, cmd: str, use_project_path=True):
        os.chdir(self.project_path if use_project_path else self.path)
        run_command(description, self.get_cmd(cmd))

    def get_cmd(self, cmd: str) -> list[str]:
        return [cmd]

    def run(self):
        skip_git = self.language.run(self)
        if not skip_git:
            self.setup_git()
        self.open_vscode()

    def make_file(self, path: str, content: str):
        with open(Path(self.project_path).joinpath(path), "w") as f:
            f.write(content)

    def append_file(self, path: str, content: str):
        with open(Path(self.project_path).joinpath(path), "a") as f:
            f.write(content)

    def make_project_dir(self):
        Path(self.project_path).mkdir(parents=True, exist_ok=True)

    def setup_git(self) -> bool:
        if questionary.confirm(f"Do you want to setup git repo?").ask():
            self.run_command("Setting up repo...", "git init")
            self.run_command("Setting up repo...",
                             'git add .')
            self.run_command("Setting up repo...",
                             'git commit -m "Project setup 🚀"')

    def open_vscode(self):
        os.chdir(self.project_path)
        if questionary.confirm(f"Do you want to open vscode?").ask():
            os.system("code .")


CLASS = Default

import enum
import os
from pathlib import Path
from typing import Optional
import typer
from rich import print
import questionary

from .config import APP_NAME, LANGUAGES
from .setting import Settings

from questionary import Validator, ValidationError, prompt

from .util import run_command

Language = enum.Enum('Language', dict([
    (k, k) for k in LANGUAGES
]))

app = typer.Typer()


@app.command()
def main(language: Optional[Language] = None, path: Optional[Path] = None, name: Optional[str] = None):
    print(f"****    [bold green]{APP_NAME}[/bold green]    ****")

    try:
        language = get_lang(language)
        path = get_path(language, path)
        name = get_name(name)

        skip_git, project_path = LANGUAGES[language.value](path, name)

        if not skip_git:
            setup_git(project_path)

        open_vscode(project_path)
    except:
        pass


def setup_git(project_path):
    os.chdir(project_path)
    if questionary.confirm(f"Do you want to setup git repo?").ask():
        run_command("Setting up repo...", "git", "init")
        run_command("Setting up repo...", "git", "config", "--global", "--add", "safe.directory",
                    project_path.__repr__())
        run_command("Setting up repo...", "git", "add", ".")
        run_command("Setting up repo...", "git", "commit", "-m", "Project setup 🚀")


def open_vscode(project_path):
    os.chdir(project_path)
    if questionary.confirm(f"Do you want to open vscode?").ask():
        os.system("code .")


def get_lang(language: Language):
    if language is None:
        language = Language(questionary.select(
            "What language you want to use today?",
            choices=[member.name for member in Language],
        ).ask())
    return language


def get_path(language: Language, path: Path):
    if path is not None:
        return path

    answer = questionary.select("Where do you want to create project?", choices=[
        "Default projects path",
        "Here",
        "Other path"
    ]).ask()

    if answer == "Default projects path":
        if (path := Settings().get(language.value + "_path")) is None:
            print(f"You don't have setup default path for {language.value}.")
            path = questionary.path(f"To what path set it?").ask()
            Settings().set(language.value + "_path", path)
        return Path(path)
    elif answer == "Here":
        return Path(os.getcwd())
    else:
        path = questionary.path(f"So where do you want to create this project?").ask()
        return Path(path)


def get_name(name):
    class NameValidator(Validator):
        def validate(self, document):
            if len(document.text) < 1:
                raise ValidationError(
                    message="Please enter a name",
                    cursor_position=len(document.text),
                )

    if name is None:
        name = questionary.text("How do you wanna call this project?", validate=NameValidator).ask()
    return name


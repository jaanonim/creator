
from .setting import Settings
from .runners.default import Default
import os
from pathlib import Path
import questionary
from rich import print


def get_runner() -> Default:
    from .config import RUNNER, _RUNNERS
    if Settings().get("runner") is not None:
        return _RUNNERS[Settings().get("runner")]

    runner = RUNNER(questionary.select(
        "What runner you want to use?",
        choices=[member.name for member in RUNNER],
    ).ask())

    if questionary.confirm(f"Do you want to save this runner as default?").ask():
        Settings().set("runner", runner.name)
    return _RUNNERS[runner.value]


def get_lang(language):
    from .config import LANGUAGE, _LANGUAGES
    if language is None:
        language = LANGUAGE(questionary.select(
            "What language you want to use today?",
            choices=[member.name for member in LANGUAGE],
        ).ask())
    return _LANGUAGES[language.value]


def get_path(language, path: Path):
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
        path = questionary.path(
            f"So where do you want to create this project?").ask()
        return Path(path)


def get_name(name):
    class NameValidator(questionary.Validator):
        def validate(self, document):
            if len(document.text) < 1:
                raise questionary.ValidationError(
                    message="Please enter a name",
                    cursor_position=len(document.text),
                )

    if name is None:
        name = questionary.text(
            "How do you wanna call this project?", validate=NameValidator).ask()
    return name

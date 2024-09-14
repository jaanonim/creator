import enum
from pathlib import Path
from typing import Optional

import typer
from rich import print

from .util import get_lang, get_name, get_path, get_runner

from .config import APP_NAME, LANGUAGE
from .setting import Settings

app = typer.Typer()


@app.command()
def main(language: Optional[LANGUAGE] = None, path: Optional[Path] = None, name: Optional[str] = None):
    print(f"****    [bold green]{APP_NAME}[/bold green]    ****")

    try:
        runner = get_runner()
        language = get_lang(language)
        path = get_path(language, path)
        name = get_name(name)

        runner(language, path, name).run()

    except Exception as e:
        print(f"****    [bold red]Error:[/bold red]    ****\n")
        raise e


@app.command()
def reset():
    Settings().reset()
    print("Reset done")

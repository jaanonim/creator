import json
from pathlib import Path

import typer
from rich.console import Console

from .config import APP_NAME

err_console = Console(stderr=True)


class Settings:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance._init()
        return cls.__instance

    def _init(self):
        app_dir = Path(typer.get_app_dir(APP_NAME))
        app_dir.mkdir(parents=True, exist_ok=True)
        self.path: Path = app_dir / "config.json"

        self.data = {}
        try:
            f = open(self.path)
            self.data = json.load(f)
            f.close()
            if self.data == {}:
                raise Exception
        except:
            err_console.print(f"Settings: Cannot found {self.path}")
            print("Creating new config file...")
            with open(self.path, "w") as json_file:
                json.dump({}, json_file)

    def get(self, name):
        return self.data.get(name)

    def set(self, name, value):
        self.data[name] = value
        with open(self.path, "w") as json_file:
            json.dump(self.data, json_file)

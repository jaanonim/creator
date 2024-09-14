
from rich.progress import Progress, SpinnerColumn, TextColumn

from rich.console import Console
import subprocess

err_console = Console(stderr=True)


def run_command(description: str, cmd: list[str]):
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
    ) as progress:
        progress.add_task(description=description)
        while proc.poll() is None:
            pass

    if proc.poll() != 0:
        log, error = proc.communicate()
        print(log)

        print("[red bold]Error[/red bold]")
        err_console.print(error)

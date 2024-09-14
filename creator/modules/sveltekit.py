import questionary
from ..runners.default import Default


def run(runner: Default):
    runner.run_command_interactive(
        f"pnpm create svelte@latest {runner.name}", use_project_path=False)

    if questionary.confirm(f"To what to install dependencies?").ask():
        runner.run_command("Installing dependencies...", "pnpm i")

    return False


DEPS = ["nodejs", "pnpm"]

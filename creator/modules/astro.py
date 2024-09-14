from ..runners.default import Default


def run(runner: Default):
    runner.run_command_interactive(
        f"pnpm create astro@latest {runner.name}", use_project_path=False)
    return True


DEPS = ["nodejs", "pnpm"]

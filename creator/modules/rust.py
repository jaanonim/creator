from ..runners.default import Default


def run(runner: Default):
    runner.make_project_dir()

    runner.run_command("Creating project...", "cargo init")
    runner.make_file("README.md", f"# {runner.name}\n")

    return False


DEPS = ["rustc", "cargo", "gcc", "rustfmt", "clippy", "rustup"]

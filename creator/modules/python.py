from ..runners.default import Default


def run(runner: Default):
    runner.make_project_dir()

    runner.make_file(
        "main.py", '\ndef main():\n\tpass\n\n\nif __name__ == "__main__":\n\tmain()\n')

    runner.make_file("requirements.txt", "")

    runner.make_file("README.md", f"# {runner.name}\n")
    runner.make_file(".gitignore", "env\n.vscode\n__pycache__\n.idea\n")

    runner.run_command("Creating env...", "python3 -m venv venv")
    return False


DEPS = ["python3", "python3.pkgs.pip"]

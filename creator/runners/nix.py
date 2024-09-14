import os
from pathlib import Path

import questionary

from .default import Default

PART_1 = '''
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      # packages.${system}.default = ...
      devShells.${system}.default =
        pkgs.mkShell
          {
            nativeBuildInputs = with pkgs; ['''

PART_2 = '''
            ];
          };
    };
}
'''


class Nix(Default):
    def __init__(self, language, path: str, name: str):
        super().__init__(language, path, name)
        self.deps = language.DEPS + ["git", "nix"]

    def run_command_interactive(self, cmd: str, use_project_path=True):
        os.chdir(self.project_path if use_project_path else self.path)
        # TODO: Running in interactive mode breaks other commands
        os.system(" ".join(self.get_cmd(cmd)))

    def get_cmd(self, cmd: str):
        return ["nix-shell", "-p", *self.deps, "--run", f'"{cmd}"']

    def make_flake(self):
        SEP = "\n              "
        with open(self.project_path / "flake.nix", "w") as f:
            f.write("{\n  " + f'description = "{self.name} flake";' +
                    PART_1 + SEP + SEP.join(self.deps) + PART_2)

    def generate_lock(self):
        git = os.path.isdir('.git')

        if git:
            self.run_command("Creating flake...", "git add .")
        self.run_command("Creating flake...", "nix flake lock")
        if git:
            self.run_command("Creating flake...",
                             'git add .')
            self.run_command("Creating flake...",
                             'git commit -m "Setup for nix"')

    def direnv(self):
        if questionary.confirm(f"Use direnv?").ask():
            self.make_file(".envrc", "use flake\n")
            self.append_file(".gitignore", "\n.envrc\n.direnv\n")

            self.run_command("Allow direnv...", "direnv allow")

    def run(self):
        skip_git = self.language.run(self)
        if not skip_git:
            self.setup_git()
        self.make_flake()
        self.direnv()
        self.generate_lock()
        self.open_vscode()


CLASS = Nix

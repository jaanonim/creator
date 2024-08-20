{
  description = "Creator flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs = {
    self,
    nixpkgs,
    poetry2nix,
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      config.allowUnfree = true;
    };
    inherit (poetry2nix.lib.mkPoetry2Nix {inherit pkgs;}) mkPoetryApplication;
  in {
    packages.${system}.default = mkPoetryApplication {
      name = "creator";
      projectDir = ./.;

      buildInputs = with pkgs; [
        git
        pnpm
        python3
        cargo
        vscode
      ];
    };
    devShells.${system} = import ./shell.nix nixpkgs.legacyPackages.${system};
  };
}

{
  description = "Creator flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs =
    { self
    , nixpkgs
    , poetry2nix
    ,
    }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
      lib = pkgs.lib;
      inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication;
    in
    {
      packages.${system}.default = mkPoetryApplication {
        name = "creator";
        projectDir = ./.;

        postFixup = ''
          wrapProgram $out/bin/creator \
            --set PATH ${lib.makeBinPath( with pkgs; [
              git
              nodejs
              pnpm
              python3
              cargo
              vscode
              direnv
              gnused
              coreutils
              nix
            ])}
        '';
      };
      devShells.${system}.default =
        pkgs.mkShell
          {
            nativeBuildInputs = with pkgs; [
              python3
              python3.pkgs.pip
              poetry
            ];
          };
    };
}

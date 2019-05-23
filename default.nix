with import ~/Documents/Code/nixpkgs/default.nix {};

stdenv.mkDerivation rec {
  name = "vacation-env";

  buildInputs = [
    (python37.withPackages (ps: [
      ps.yapf
      ps.click
      ps.pep8
    ]))
    mypy
  ];
}


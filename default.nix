with import ~/Documents/Code/nixpkgs/default.nix {};

stdenv.mkDerivation rec {
  name = "vacation-env";

  buildInputs = [
    (python36.withPackages (ps: [
      ps.yapf
      ps.click
      ps.pep8
    ]))
  ];
}


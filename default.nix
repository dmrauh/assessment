with import <nixpkgs> { };

stdenv.mkDerivation rec {
  name = "assessment-env";

  buildInputs = [
    (python3.withPackages (ps: with ps; [ click ]))
    python3Packages.mypy
    python3Packages.yapf
  ];
}


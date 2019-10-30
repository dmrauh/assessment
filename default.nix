with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "assessment-env";

  buildInputs = [
    (python3.withPackages (ps: [
      ps.yapf
      ps.click
      ps.pep8
    ]))
    mypy
  ];
}


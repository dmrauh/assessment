with import <nixpkgs> { };

stdenv.mkDerivation rec {
  name = "assessment-env";

  buildInputs = [ (python3.withPackages (ps: with ps; [ click ])) ]
    ++ (with python3Packages; [ ipython mypy yapf ]);
}


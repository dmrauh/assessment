with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "assessment-env";
  buildInputs = [
    # System requirements.
    readline

    # Python requirements (enough to get a virtualenv going).
    (python3.withPackages (ps: with ps; [click hypothesis] ))
    python3Packages.virtualenv
    python3Packages.pip
    python3Packages.pytest
  ];
  src = null;
  shellHook = ''
    # Allow the use of wheels.
    SOURCE_DATE_EPOCH=$(date +%s)

    # Augment the dynamic linker path
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${R}/lib/R/lib:${readline}/lib
  '';
}


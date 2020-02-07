with import <nixpkgs> {};
with pkgs.python3Packages;

buildPythonPackage rec {
  name = "assessment";
  src = ./.;
  propagatedBuildInputs = [ click ];
}


set -e
pynml-modchananalysis kdrmt -stepV 5 -temperature [28,35] -nogui
pynml-modchananalysis kamt -stepV 5 -temperature [28,35] -nogui
pynml-modchananalysis nax -stepV 5 -temperature [28,35] -modFile naxn.mod -dt 0.0025 -nogui

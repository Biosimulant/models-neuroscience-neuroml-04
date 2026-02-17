#!/bin/bash
set -ex

### A script to validate SBML & SED-ML files using pyNeuroML

pynml -validate-sbml *.xml

echo "All XML files are valid SBML"

pynml -validate-sedml *.sedml

echo "All SED-ML files are valid"
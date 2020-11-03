#!/bin/bash
# =================================
cd $(dirname "$0") && cd $(dirname ${PWD}) && cd $(dirname ${PWD})
# =================================

# package_files=$(find ${PWD}/package/ -type f | paste -sd ":" -)
# export PYTHONPATH="${PWD}:${package_files}"
export PYTHONPATH="${PWD}"

python $@

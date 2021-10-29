#!/bin/bash

# Delete python build artifacts in this directory
rm -rf ./dist
rm -rf ./build
rm -rf ./*.egg-info

# Delete compiled python package-wide
find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

### Hexlet tests, Developer tests, Linter status, Maintainability, Test Coverage:
[![Actions Status](https://github.com/Abra19/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Abra19/python-project-50/actions)
[![Python CI](https://github.com/Abra19/python-project-50/actions/workflows/python_ci.yml/badge.svg)](https://github.com/Abra19/python-project-50/actions/workflows/python_ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/59cc52fc12a5afd4759f/maintainability)](https://codeclimate.com/github/Abra19/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/59cc52fc12a5afd4759f/test_coverage)](https://codeclimate.com/github/Abra19/python-project-50/test_coverage)

### Descriptions
This project implements a function gendiff that compare two configuration files and show a difference.

To compare files, you need to pass to the function gendff two args: ../path/to/file1, ../path/to/file2.

The path to the file can be either relative: ../somefile or absolute /somedir/somefile.

The function can be used as a library or as a console utility
  
### Requirements
1. Python >=3.11
2. pip >= 19
3. poetry >= 1.2.0

### To get started
1. Clone git repo:
  `git clone git@github.com:Abra19/python-project-50.git`
2. Go to directory python-project-50:
  `cd python-project-50`
3.  Configuring `poetry` to create a virtual environment:
  `poetry config virtualenvs.in-project true`
4.  Create virual environment and Install dependencies
  `make install`
5. Build package
  `make build`
6. Publish package:
  `make publish`
7. Installing the package in the user's environment:
  `make package-install`
8. If you receive a tracking warning at step 7:
  `WARNING: The script gendiff is installed in 'path/to/your/executable' which is not on PATH.`
  Add this directory to PATH:
  `export PATH=$PATH:'path/to/your/executable'`

### To Run
Stylish formatter(default) for plain trees:

[![asciicast](https://asciinema.org/a/QNWeY8JDMg4A7dInevCVWVNmp.svg)](https://asciinema.org/a/QNWeY8JDMg4A7dInevCVWVNmp)

Stylish formatter(default) for nested trees:

[![asciicast](https://asciinema.org/a/OGoq9EpzV2QfgWEw2AkK0sXsY.svg)](https://asciinema.org/a/OGoq9EpzV2QfgWEw2AkK0sXsY)

Plain formatter for nested trees:

[![asciicast](https://asciinema.org/a/arW8NSJ7hxdGmGfcHdqk1ggK9.svg)](https://asciinema.org/a/arW8NSJ7hxdGmGfcHdqk1ggK9)

Json formatter for nested trees:

[![asciicast](https://asciinema.org/a/kJdxJMREqoLFk7rCNIbkpkmOV.svg)](https://asciinema.org/a/kJdxJMREqoLFk7rCNIbkpkmOV)

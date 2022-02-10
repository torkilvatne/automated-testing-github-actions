# Automated testing with GitHub Actions

<div id="top"></div>

![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)

## Getting Started

This is an example of how to use GitHub Actions for automated testing.

To install and set up the project clone the repo and run:

   ```sh
   pip install -e .
   ```

To install pre-commit run:

   ```sh
   pre-commit install
   ```

# Testing

The project is set up with pytest, flake8, mypy and tox. The tests are automatically ran by GitHub Actions after push,
but can also be ran by running:

   ```sh
   pytest
   ```

or

   ```sh
   flake8 src
   ```

or

   ```sh
   mypy src
   ```

or

   ```sh
   tox
   ```

Tox build isolated environments based on different Python versions, so that will take longer time. It will not run if
the right Python version is not installed on the computer.

# Used libraries

* General package structure
* pytest
* flake8
* mypy
* tox
* pre-commit

* <p align="right">(<a href="#top">back to top</a>)</p>

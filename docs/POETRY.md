# New to Poetry


**What is it?** Python packaging and dependency management made easy

**Why?** Replace `Pip` and `conda` and ensures that `if it works on my machine, it works on your machine`.

## Table of content
<!-- TOC -->
* [Poetry-specific files](#poetry-specific-files)
  * [`pyproject.toml`](#pyprojecttoml)
  * [`poetry.toml`](#poetrytoml)
* [Basic commands](#basic-commands)
* [Building and publishing package](#building-and-publishing-package)
  * [Publishing using a tracker](#publishing-using-a-tracker)
    * [Internal package](#internal-package)
  * [Publish on GitHub](#publish-on-github)
* [Poetry dependency groups](#poetry-dependency-groups)
* [Sub packages](#sub-packages)
* [Handle Python versions :cold_sweat:](#handle-python-versions--coldsweat-)
* [Pre-commit hooks](#pre-commit-hooks)
<!-- TOC -->

## Poetry-specific files

### `pyproject.toml`
Main file containing the supported Python versions(s), virtual environment information and dependencies.

````toml
[tool.poetry]

# General information about the project / package
name="the name of the package"
version = "1.0.0"
description = "a short description of the package"
authors = ["name of the author <email of the author>"]

# Optional, used for packaging, e.g.:
packages = [
    { include = "package_name", from = "src" },
]

# Dependencies at a high-level.
# It details the Python version(s) required to use the repo
# and the packages / libraries and their acceptable version.
[tool.poetry.dependencies]
python = "^3.8"
pandas = ">=2.0"
pandera = {extras = ["pyspark"], version = "^0.13.4"}

# Automatically generated by Poetry, don't touch without any good reasons
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
````

### `poetry.toml`
Additional Poetry configs.

````toml
[virtualenvs]
create = true
# Create the venv in the project
in-project = true
# Specifiy the venv location
path = "{project-dir}/.venv"
prefer-active-python = true
# Specify the terminal venv prompt
prompt = "{project_name}-py{python_version}"
````

## Basic commands

- `poetry install`: create a venv and install the dependencies
- `poetry add <package>`: equivalent to `pip install`

> Note
> poetry will first check that all packages and their dependencies that are in the project are compatible with each other. This means that poetry will try to find a combination of package versions that satisfies all the version requirements / restrictions of all packages in the project. If such a combination is found, poetry generates / updates the poetry.lock file that "pins" these exact versions.

- `poetry remove <package>`: similar to `pip uninstall`

> Note
> An important difference with pip is that the dependencies of the removed package that are no longer referenced will also be removed. After this is done, the poetry.lock file is updated.

- `poetry update [<package>]`: updates a package (if provided) or all packages in the project and their dependencies to the highest versions that satisfies the version requirements of all packages in the project. After resolving the dependencies, the poetry.lock file is updated.
- `poetry show`: equivalent to `pip list`. If `--tree` argument is specified, the output is more detailed,

```
$ poetry show --tree
requests-toolbelt 0.8.0 A utility belt for advanced users...
└── requests <3.0.0,>=2.0.1
    ├── certifi >=2017.4.17
    ├── chardet >=3.0.2,<3.1.0
    ├── idna >=2.5,<2.7
    └── urllib3 <1.23,>=1.21.1
```

- `poetry run <command>`: allows running command within the python environment. It also ensures that this command is run within the Poetry python environnement.

## Building and publishing package
The `poetry build` command will create a wheel (`.whl`) and a sdist (`.tar.gz`) file in the `/dist` folder in the project root.
They can be used to install the project package in another environment or to distribute the package using a tracker such as PyPi.

### Publishing using a tracker
Use the `poetry publish` command.
This will prompt for a PyPi username and password.

#### Internal package
We should use the internal Ivado Labs tracker. This is specified in the `pyproject.toml`.

````toml
[[tool.poetry.source]]
name = 'private'
url = 'http://example.com/example'
````

Then one can use the `poetry publish -r private` command.

To avoid any accidental PyPi release, add the following code to the `[tool.poetry]` section:
````toml
classifiers = [
    "Private :: Do Not Upload",
]
````

### Publish on GitHub
Create a release on GitHub and upload the `.whl` and `.tar.gz` files.
The package is then available to be added in another repo by using the following command in the other repo:

```
poetry add git+https://github.com/ivadolabs/repo-name.git#main
```

## Poetry dependency groups
Instead of using files like `requirements-dev.txt`, Poetry support dependency groups that can be used as follows.
```
poetry add pre-commit --group dev
poetry add sphinx --group docs
poetry add pytest --group test

# then one can install by running
poetry install
# or
poetry install --without dev
# or even
poetry install --only dev
```

If you want those dependency groups to be optional, be sure to add the following parameter under your group, for example:

```toml
[tool.poetry.group.docs]
optional = true
```
Then one can install the optional group by running:
```
poetry install --with docs
```

## Sub packages
Under root, one can have multiple packages, each with their own poetry environment.
Here's an example of the `pyproject.toml`:

````toml
[tool.poetry.dependencies]
python = ">=3.8,<3.12"

# 3 sub-packages
feature-engineering = { path = "feature_engineering/" }
model = { path = "model/" }
shared_utils = { path = "shared_utils/" }
````

## Handle Python versions :cold_sweat:
When your Poetry Python version requirement doesn't match your local Python version, please use Pyenv.
First install it by running:
```bash
brew update
brew install pyenv
```

Then, Pyenv allows you to install and handle multiple versions of Python.
To install a new one run:
```
pyenv install 3.11.0
```

Then, you can set it as the local or global version by running:
```
pyenv global 3.11.0
# or
pyenv local 3.11.0
```

Before running `poetry install`, you can run the following command to tell Poetry which Python version to use:
```
poetry env use python3.11.0
```

## Pre-commit hooks
You should always add the following Poetry pre-commits.

- `poetry-check` hook: make sure the poetry configuration does not get committed in a broken state.

If one commits the `petry.lock` file, then
- `poetry-lock` hook: make sure the lock file is up to date when committing changes.

For the old schooled ones,
- `poetry-export` hook: export command to sync your `requirements.txt` file with your current dependencies.

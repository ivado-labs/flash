[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
![Coverage](coverage.svg)

> [!IMPORTANT]
>
> If you want to know the template's full set of features, read [this](docs/TEMPLATE.md).
>
> Before going forward,
>
> - Rename the [project_name](project_name) folder name. Also, apply this rename to the `--source=project_name` argument in the [Makefile](Makefile)'s `coverage` command.
>
> - Rename the `name` under `tool.poetry` in [pyproject.yml](pyproject.toml).
>
> - Rename the [PROJECT NAME](#project-name) in this `README`.
>
> - Make sure that your GitHub Actions workflow permissions are set to `Read and write` (see `Settings` > `Actions` > `General` > `Workflow permissions` > `Read and write permissions`).
>
> - Make sure that your GitHub settings Dependabot are enabled (see `Settings` > `Security` > `Code security and analysis` > `Enable them all`).
>
> - Add the `bot-project-template` user to the project collaborators with `Write` access (see `Settings` > `Access` > `Collaborators and teams`).
>
> - Modify the [CODEOWNERS](CODEOWNERS) file by adding your team members or GitHub group.
>
> - To enable GitHub's Slack notifications. Open the development Slack channel of your project (create one if needed). Write `/github subscribe [repository name]`. See [doc](https://github.com/integrations/slack?tab=readme-ov-file#installation) for more details and customization.
>
> - Delete this section.

# PROJECT NAME
...

## Install

This project requires the following to be installed:
- [Poetry](https://python-poetry.org/docs/#installation) to manage dependencies. If you are new to Poetry, please read the [New to Poetry](docs/POETRY.md) documentation.
- [Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to manage Python versions.

Then, to proceed with the setup, run:
```bash
make setup
```

For a list of `make` commands, run:
```bash
make help
```

## Usage
...

## Docs
- [Conventions](docs/CONVENTIONS.md): project code convention to follow.
- [New to Poetry](docs/POETRY.md): information on what Poetry is and how to use it.

# What does the project template offer?

Here's the list of what the Python Project Template offers for your project.

- A Common project structure
- Pre-built [`README`](../README.md) with relevant badges (some are auto-updated during CI, such as for the Code Coverage).
- Common Python [setup](../Makefile), using Poetry and Pyenv, ensures the Python version is the right one and the  `venv` is at the same place for everyone.
- A [pre-commit file](../.pre-commit-config.yaml) with Ivado Labs standards
  - Mainly using Ruff with a thoroughly handpicked set of rules and configurations
- A [`CODEOWNERS`](../CODEOWNERS) file to simplify your PR review process.
- A simple way to add repository notifications using Ivado Labs' pre-set Slack app.
- A [bot](../.github/dependabot.yml) (dependabot) to automatically create PRs to update your project versions (e.g., Python package, GitHub workflow, etc.).
- Pre-built GitHub workflows
  - **[CI](../.github/workflows/ci.yaml):** common checks for PRs
  - **[Release](../.github/workflows/release.yml):** creates a `release` branch, automatically assigns a tag and publishes to GitHub
  - **[Hotfix](../.github/workflows/hotfix.yml):** automatically assign a tagging when a PR is merged into a `release` branch
  - **[Sync-template](../.github/workflows/sync-template.yml):** weekly automatic PR, with the latest changes to the template, sent to all projects created from this template
- [Centralized documentation](../docs) on key concepts, such as Ivado Labs Git flow, branch & commit conventions

> [!IMPORTANT]
> This template is a **company initiative**, meaning that if you want to participate, you are more than welcome!
> Create a PR or an issue and share it with others.
> The perfect state would be a template perfectly aligned with Ivado Labs' requirements.

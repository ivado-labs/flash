[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
![Coverage](coverage.svg)

<h1>
   <img src="https://github.com/user-attachments/assets/adc9f12a-7f98-4c93-b35d-f034f38c8030" width="70" height="70" > Flash initiative
</h1>

The primary objective of the Flash initiative is to equip you with a toolkit that enhances the speed and efficiency of your daily tasks as a Data Scientist!

The tools in our curated list are selected based on a couple of criteria:

- 👥 Relevance to Ivado Labs projects. Qualitative value: low, medium, high.
- 👨‍💻 Ease of use/installation. Qualitative value: low, medium, high.
- 📖 Quality of the available documentation. Qualitative value: low, medium, high.
- 🥇🥈🥉 (if applicable) Project quality score from [best of ML](https://github.com/ml-tooling/best-of-ml-python) initiative. Quantitative value.
- ⭐ (if applicable) GitHub Star Count. Quantitative value.

## Toolbox

Below is a list of the tools we tested or are actively testing:

| Category          | Tool         | Description                                                                                                                   |     Status      | 👥       | 👨‍💻 | 📖 | 🥇🥈🥉 |  ⭐   | Quick tutorial    |
|-------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------|:---------------:|----------|-----|----|:------:|:----:|----------------------|
| Auto ML           | PyCaret      | PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows.             |    Tested ✅     |   ⏳ |  ⏳ |  ⏳ |   37   | 8.6K | Available [here](/notebooks/ML/AutoML/PyCaret/README.md) |
| Time series       | Nixtla       | A set of our open-source libraries designed to provide a comprehensive, cutting-edge toolkit for time series forecasting.    |  In progress ⏳  |  ⏳  | ⏳ | ⏳ |   34   | 3.6K | Not available yet !     |
| Data exploration  | Data Wrangler | Data Wrangler is a code-centric data viewing and cleaning tool integrated into VS Code and VS Code Jupyter Notebooks. |  In progress ⏳  |  ⏳  | ⏳|⏳ |  N/A   | N/A  | Not available yet !     |
| Data manipulation | ydata-quality | An open-source python library for assessing Data Quality throughout the multiple stages of a data pipeline development.       | In progress ⏳   |   ⏳ | ⏳ | ⏳ |  N/A  | 420  |  Not available yet !  |

We also have a couple of tools in our backlog that we are planning to test:

| Category         | Tool             | Description                                                                             |
|------------------|------------------|-----------------------------------------------------------------------------------------|
| Data Exploration | ydata-profilling | An open-source python library for Data quality profiling and exploratory data analysis. |
| General          | Quatro           | An open-source scientific and technical publishing system.                              |


## Contribution
You have a suggestion or want to contribute to the Flash initiative?

Don't hesitate to reach out in our Slack channel [#flash-initiative](https://ivadolabscommittee.slack.com/archives/C06QXHPRLMR)!

## Installation steps (WIP)

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

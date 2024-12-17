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

| Category          | Tool         | Description                                                                                                               |     Status      | 👥       | 👨‍💻 | 📖 | 🥇🥈🥉 |  ⭐   | Quick tutorial    |
|-------------------|--------------|---------------------------------------------------------------------------------------------------------------------------|:---------------:|----------|-----|----|:------:|:----:|----------------------|
| Data Exploration | ydata-profilling | An open-source Python library used to generate an exploratory data analysis (EDA) report with just a few lines of code.|    Tested ✅     |   High |  High |  Medium |   35   | 13K  | Available [here](./notebooks/EDA/pandas-profiling/README.md) |
| Auto ML           | PyCaret      | PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows.         |    Tested ✅     |   High |  High |  High |   37   | 8.6K | Available [here](./notebooks/ML/AutoML/PyCaret/README.md) |
| Time series       | Nixtla       | A set of our open-source libraries designed to provide a comprehensive, cutting-edge toolkit for time series forecasting. |  Tested ✅    | High | High | Medium |   34   | 3.6K |Available [here](./notebooks/ML/NixtlaREADME.md) |    |
| Data exploration  | Data Wrangler | Data Wrangler is a code-centric data viewing and cleaning tool integrated into VS Code and VS Code Jupyter Notebooks.     |  In progress ⏳  |  ⏳  | ⏳|⏳ |  N/A   | N/A  | Not available yet !     |
| Data manipulation | ydata-quality | An open-source Python library for assessing Data Quality throughout the multiple stages of a data pipeline development.   | In progress ⏳   |   ⏳ | ⏳ | ⏳ |  N/A   | 420  |  Not available yet !  |

We also have a couple of tools in our backlog that we are planning to test:

| Category         | Tool             | Description                                                                             |
|------------------|------------------|-----------------------------------------------------------------------------------------|
| General          | Quatro           | An open-source scientific and technical publishing system.                              |


## Setup

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

## Contribution

Contributions are encouraged and always welcome!

If you want to add a new tool, you can:
- Duplicate the [README](notebooks/TEMPLATE/README.md) and [introduction notebook](notebooks/TEMPLATE/intro_tutorial.ipynb) in the appropriate folder.
- Fill up those files and submit a pull request.

You have a suggestion or want to contribute to the Flash initiative? Don't hesitate to reach out in our Slack channel [#flash-initiative](https://ivadolabscommittee.slack.com/archives/C06QXHPRLMR)!

> [!IMPORTANT]
> When creating a new branch, if you get this error :
> ```bash
> <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
> ```
> Run the following:
> ```bash
> export SSL_CERT_FILE=$(poetry run python -c "import certifi; print(certifi.where())")
> echo 'export SSL_CERT_FILE=$(poetry run python -c "import certifi; print(certifi.where())")' >> ~/.zshrc
> poetry run pre-commit clean
> poetry run pre-commit install
> poetry run pre-commit run
> ```

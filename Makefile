.DEFAULT_GOAL := help
PYTHON_VERSION := $(shell cat .python-version)


.PHONY: install-python
install-python: ## Install the specified Python version
	@if [ -n "$$(pyenv versions | grep $(PYTHON_VERSION))" ]; then \
	  echo "Requirement Python $(PYTHON_VERSION): already installed."; \
	else \
	  pyenv install $(PYTHON_VERSION) && \
	  pyenv local $(PYTHON_VERSION) && \
	  echo "Requirement Python $(PYTHON_VERSION): installed."; \
	fi

.PHONY: setup
setup: install-python ## Setup the project for the first time
	poetry env use $(PYTHON_VERSION)
	poetry install
	poetry run pre-commit install

	# add PYTHONPATH to .env for things like Jupyter
	echo "PYTHONPATH=${PWD}" >> .env

.PHONY: coverage
coverage: ## Run pytest test coverage
	poetry run coverage run --source=project_name -m pytest && poetry run coverage report

# automatic Makefile help generator proposed by https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

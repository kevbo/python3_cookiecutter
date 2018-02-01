PYTHON = $(ENV)/bin/python3
ENV = $(CURDIR)/env
COVERAGE = $(ENV)/bin/coverage


deps:
	pipenv install --dev

shell: deps
	pipenv run bpython

start: deps
	pipenv run tmuxp load .

test: deps
	pipenv run coverage run -m unittest
	pipenv run coverage report -m
	pipenv run coverage xml
	pipenv check
	pipenv check --style *.py

ci-install:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

outdated: deps
	pipenv run pip list --outdated

clean:
	pipenv --rm

.PHONY: deps shell start clean test coverage pep8 outdated

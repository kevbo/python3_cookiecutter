PYTHON = $(ENV)/bin/python3
ENV = $(CURDIR)/env
COVERAGE = $(ENV)/bin/coverage


env:
	python3 -m venv $(ENV)

deps: env
	$(ENV)/bin/pip install -U pip setuptools
	$(ENV)/bin/pip install -r requirements.txt

shell: deps
	$(ENV)/bin/bpython

start: deps
	$(ENV)/bin/tmuxp load .

test: deps
	$(PYTHON) -m unittest

coverage: deps
	$(COVERAGE) erase
	$(COVERAGE) run --omit test* -m unittest
	$(COVERAGE) report

pep8:
	$(ENV)/bin/pep8 *.py

outdated:
	$(ENV)/bin/pip list --outdated

clean:
	rm -rf env

.PHONY: deps shell start clean test coverage pep8 outdated

PYTHON = $(ENV)/bin/python3
ENV = $(CURDIR)/env

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

clean:
	rm -rf env

.PHONY: deps shell start clean

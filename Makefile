# Tareas locales
ifeq ($(OS),Windows_NT)
	PY := .venv/Scripts/python.exe
	PIP := .venv/Scripts/pip.exe
else
	PY := .venv/bin/python
	PIP := .venv/bin/pip
endif

.PHONY: setup lint format test

setup:
	python -m venv .venv
	$(PY) -m pip install -U pip
	$(PIP) install ruff pytest

lint:
	$(PY) -m ruff check .

format:
	$(PY) -m ruff format .

test:
	$(PY) -m pytest -q

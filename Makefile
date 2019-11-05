#!/usr/bin/env make

venv-init:
	pipenv shell

coverage:
	coverage report

clean:
	rm -rf ./**/__pycache__
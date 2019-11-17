#!/usr/bin/env make

venv-init:
	pipenv shell

test:
	pytest

clean:
	rm -rf ./**/__pycache__
	rm -rf ./**/*.pyc

rootize:
	chown root:root ./tests/root_access
	chmod 650 ./tests/root_access

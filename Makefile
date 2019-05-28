#!/usr/bin/env make

venv-init:
	pipenv --python 3.6 shell

venv-activate:
	pipenv shell

unittest:
	cd main && \
	coverage run -m unittest tests.test_dup.TestDup && \
	coverage report -m

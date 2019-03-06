#!/usr/bin/env make

unittest:
	cd main && \
	coverage run -m unittest tests.test_dup.TestDup && \
	coverage report -m
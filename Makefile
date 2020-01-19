#!/usr/bin/env make

venv-init:
	pipenv shell

test:
	pytest

clean:
	rm -rf ./**/__pycache__
	rm -rf ./**/*.pyc

# doesnt work
sample-directory:
	mkdir -p sample_directory
	mkdir -p sample_directory/1file
	echo 'hi' > sample_directory/1file/xd.txt
	mkdir -p sample_directory/2files
	mkdir -p sample_directory/nested_directories
	mkdir -p sample_directory/nested_directories/empty
	mkdir -p sample_directory/nested_directories/1file
	echo 'text' > sample_directory/1file/xd.txt
	mkdir -p sample_directory/nested_directories/2files
	echo 'hi' > sample_directory/2files/first.txt
	echo 'hi' > sample_directory/2files/second.txt

remove-sample_directory:
	rm -rf sample_directory
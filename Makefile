#!/usr/bin/env make

install:
	pip install -r requirements.txt

test:
	pytest

clean:
	rm -rf ./**/__pycache__
	rm -rf ./**/*.pyc

TEST_DIR=tests/sample_directory
sample-directory:
	mkdir -p ${TEST_DIR}
	mkdir -p ${TEST_DIR}/1file
	echo 'hi' > ${TEST_DIR}/1file/1.txt
	mkdir -p ${TEST_DIR}/2files
	echo 'hi' > ${TEST_DIR}/2files/first.txt
	echo 'hi' > ${TEST_DIR}/2files/second.txt
	mkdir -p ${TEST_DIR}/nested_directories
	mkdir -p ${TEST_DIR}/nested_directories/empty
	mkdir -p ${TEST_DIR}/nested_directories/1file
	echo 'hi' > ${TEST_DIR}/nested_directories/1file/file.xd
	mkdir -p ${TEST_DIR}/nested_directories/2files
	echo 'hi' > ${TEST_DIR}/nested_directories/2files/first.txt
	echo 'hi' > ${TEST_DIR}/nested_directories/2files/second.txt

remove-sample_directory:
	rm -rf ${TEST_DIR}

import pytest
from duplicate_finder import find


def test_single_dir_structure_entry():
    assert find.dir_structure('./tests/sample_directory/1file/') \
        == {
            "{'path': './tests/sample_directory/1file/1.txt', 'metadata': {'name': '1.txt', 'size': 3}}"
            }

def test_dir_structure_should_return_valid_structure():
    assert find.dir_structure('./tests/sample_directory') \
        == {
        "{'path': './tests/sample_directory/1file/1.txt', 'metadata': {'name': '1.txt', 'size': 3}}",
        "{'path': './tests/sample_directory/2files/first.txt', 'metadata': {'name': 'first.txt', 'size': 3}}",
        "{'path': './tests/sample_directory/2files/second.txt', 'metadata': {'name': 'second.txt', 'size': 3}}",
        "{'path': './tests/sample_directory/nested_directories/1file/file.xd', 'metadata': {'name': 'file.xd', 'size': 3}}",
        "{'path': './tests/sample_directory/nested_directories/2files/first.txt', 'metadata': {'name': 'first.txt', 'size': 3}}",
        "{'path': './tests/sample_directory/nested_directories/2files/second.txt', 'metadata': {'name': 'second.txt', 'size': 3}}",
        }

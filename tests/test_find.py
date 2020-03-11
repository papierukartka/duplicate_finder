import pytest
from duplicate_finder import find


def test_single_dir_structure_entry():
    assert find.dir_structure('./tests/sample_directory/1file/') \
        == {
            "{'path': './tests/sample_directory/1file/1.txt', 'metadata': {'name': '1.txt', 'size': 3}}"
            }
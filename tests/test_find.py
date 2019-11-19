import pytest
from duplicate_finder import find


def test_dir_structure_should_return_valid_structure():
    directory = {
        "{'file': './tests/sample_directory/poznan.txt', 'metadata': {'size': 5}}",
        "{'file': './tests/sample_directory/poznan/carrot.txt', 'metadata': {'size': 0}}",
        "{'file': './tests/sample_directory/poznan/poznan.txt', 'metadata': {'size': 0}}",
        "{'file': './tests/sample_directory/poznan/rot.txt', 'metadata': {'size': 0}}",
        "{'file': './tests/sample_directory/poznan/test.txt', 'metadata': {'size': 0}}",
        "{'file': './tests/sample_directory/poznan/secret/badtouch.jpg', 'metadata': {'size': 0}}",
        "{'file': './tests/sample_directory/wroclaw/pic1.txt', 'metadata': {'size': 0}}",
        "{'file': './tests/sample_directory/wroclaw/tomato.txt', 'metadata': {'size': 25}}"
    }

    assert find.dir_structure('./tests/sample_directory') == directory

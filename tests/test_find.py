import pytest
from duplicate_finder import find


def test_dir_structure_should_return_valid_structure():
    directory = [
        {
            'file': './tests/sample_directory/poznan.txt',
            'type': 'text'
        },
        {
            'file': './tests/sample_directory/poznan/carrot.txt',
            'type': '.txt',
        },
        {
            'file': './tests/sample_directory/poznan/poznan.txt',
            'type': '.txt'
        },
        {
            'file': './tests/sample_directory/poznan/rot.txt',
            'type': '.txt'
        },
        {
            'file': './tests/sample_directory/poznan/test.txt',
            'type': '.txt'
        },
        {
            'file': './tests/sample_directory/poznan/secret/badtouch.jpg',
            'type': '.jpg'
        },
        {
            'file': './tests/sample_directory/wroclaw/pic1.txt',
            'type': '.txt'
        },
        {
            'file': './tests/sample_directory/wroclaw/tomato.txt',
            'type': '.txt'
        }
    ]
    find.dir_structure('./tests/sample_directory')
    pass
import pytest
from duplicate_finder import find


def test_dir_structure_should_return_valid_structure():
    sample_directory_map = {
        'sample_directory': {
            'directories': {
                'poznan': {
                    'directories': {
                        'secret': {
                            'files': [
                                'badtouch.jpg',
                            ],
                        },
                    },
                    'files': [
                        'carrot.txt',
                        'poznan.txt',
                        'rot.txt',
                        'test.txt',
                    ],
                },
                'wroclaw': {
                    'files': [
                        'pic1.txt',
                        'tomato.txt'
                    ]
                },
            },
            'files': [
                'poznan.txt',
            ]

        }
    }
    find.dir_structure('./tests/sample_directory')
    pass
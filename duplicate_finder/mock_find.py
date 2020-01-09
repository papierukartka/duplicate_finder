from duplicate_finder import find
from unittest.mock import Mock

mock_find = Mock()

def info(file_path):
    mock_find.info = Mock()
    file_data = {
        './tests/sample_directory/poznan.txt': "metadata': {'size': 5}",
        './tests/sample_directory/poznan/carrot.txt': "metadata': {'size': 0}",
        './tests/sample_directory/poznan/poznan.txt': "metadata': {'size': 0}",
        './tests/sample_directory/poznan/rot.txt': "metadata': {'size': 0}",
        './tests/sample_directory/poznan/test.txt': "metadata': {'size': 0}",
        './tests/sample_directory/poznan/secret/badtouch.jpg': "metadata': {'size': 0}",
        './tests/sample_directory/wroclaw/pic1.txt': "metadata': {'size': 0}",
        './tests/sample_directory/wroclaw/tomato.txt': "metadata': {'size': 25}"
    }

    def _side_effect(arg):
        return file_data[arg]
    mock_find.info.side_effect = _side_effect

    return mock_find.info(file_path)

import os
from json import dumps


def dir_structure(tree_root: str) -> set:
    """
    Crawls down given directory to create a folder map. Populates map
    with file properties.

    :param tree_root: Relative path to directory tree root.
    :returns: Set of stringified dictionaries that reflect directory structure.
    """
    dir_representation = set()

    for folder, _, files in os.walk(tree_root):
        for file in files:
            file_path = os.path.join(folder, file)
            dir_representation.add(
                str(
                    {
                        'path': file_path,
                        'metadata': info(file_path)
                    }
                )
            )
    return dir_representation


def info(file_path: str) -> dict:
    """
    Find out file metadata.

    :param file_path: Path to file from to gather metadata
    :returns: Object containing field with file size
    """
    return {
        'name': os.path.basename(file_path),
        'size': os.stat(file_path).st_size,
    }

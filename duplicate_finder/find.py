import os
from json import dumps


def dir_structure(tree_root):
    """
    Crawls down given directory to create a folder map. Populates map
    with file properties.

    Parameters
    ----------
    tree_root : str
        Relative path to directory tree root.

    Returns
    -------
    dict
        Dictionary that reflects directory structure.
    """
    dir_representation = set()

    for folder, _, files in os.walk(tree_root):
        for file in files:
            file_path = os.path.join(folder, file)
            dir_representation.add(
                str(
                    {
                        'file': file_path,
                        'metadata': info(file_path)
                    }
                )
        )
    return dir_representation


def info(file_path):
    """
    Find out file metadata.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    dict
        object containing field with file size
    """
    return {
        'size': os.stat(file_path).st_size
    }

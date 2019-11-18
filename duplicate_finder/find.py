# !todo: info - what should it return?

import os
from json import dumps


def dir_structure(root):
    """
    Crawls down given directory to create a folder map. Populates map
    with file properties.

    Parameters
    ----------
    root : str
        Relative path to directory root.

    Returns
    -------
    dict
        Dictionary that reflects directory structure.
    """
    dir_representation = set()

    for folder, _, files in os.walk(root):
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


def clear(duplicates, directory):
    """
    Removes duplicates from the given directory.

    Parameters
    ----------
    directory : str
        Root directory that contains duplicates.
    duplicates : list
        List of paths to duplicates that are to be removed(looking from the root dir perspective).

    Returns
    -------
    int
        0 if everything went as intended

    """
    pass

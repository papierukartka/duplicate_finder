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
                        'size': os.stat(file_path).st_size
                    }
                )
        )
    return dir_representation


def info(file):
    """
    Find out file metadata.

    Parameters
    ----------
    file : str

    Returns
    -------
    ????
        tba
    """

    pass


def duplicates(directory):
    """
    Duplicated files in a given directory.

    Parameters
    ----------
    directory : dict
        Map of the directory to be analyzed.

    Returns
    -------
    list
        List of paths to duplicates that are to be removed(looking from the root dir perspective).
    """

    pass


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

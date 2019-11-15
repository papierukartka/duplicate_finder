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
    dir_representation = []

    walker = os.walk(root)

    for folder, subfolders, files in os.walk(root):
        for file in files:
            file_path = os.path.join(folder, file)
            dir_representation.append(
                {
                    'file': file_path,
                    'size': os.stat(file_path).st_size
                }
        )
    # tried sorting it but dict is not sortable.
    # try converting dict to str and store everything in some hashable object
    return sorted(dir_representation)


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

# def walk_recursively(dir_root, dir_object=[]):
#     for dirpath, dirnames, filenames in os.walk(dir_root):
#         file_list = []
#         for f in filenames:
#             file_metadata = {
#                 "name": f,
#                 "size": os.path.getsize(os.path.join(dirpath, f))
#             }
#             file_list.append(file_metadata)

#         dir_object.append({
#             dirpath: file_list
#         })
#         for directory in dirnames:
#             walk_recursively(os.path.join(dir_root, directory), dir_object)
#         break
#     return dir_object


# def rm_duplicates(dir_object):
#     # if duplicate found, delete second duplicate
#     # if second duplicate is the only file in a dir, delete dir also
#     pass
#     return dir_object
import os
from json import dumps

def walk_recursively(dir_root, dir_object=[]):
    for dirpath, dirnames, filenames in os.walk(dir_root):
        file_list = []
        for f in filenames:
            file_metadata = {
                "name": f,
                "size": os.path.getsize(os.path.join(dirpath, f))
            }
            file_list.append(file_metadata)

        dir_object.append({
            dirpath: file_list
        })
        for directory in dirnames:
            walk_recursively(os.path.join(dir_root, directory), dir_object)
        break
    return dir_object


def rm_duplicates(dir_object):
    # if duplicate found, delete second duplicate
    # if second duplicate is the only file in a dir, delete dir also
    pass
    return dir_object
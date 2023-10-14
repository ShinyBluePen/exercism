"""Flatten Array

https://exercism.org/tracks/python/exercises/flatten-array
"""

def flatten(array: list) -> list:
    """Return a flattened list-like structure of arbitrary depth excluding Null values.
    
    :param array: - A list of arbitrary depth.
    :return flatlist: - A list of the given `iterable` flattened to a depth of 1.
    """
    flat_list = []
    for item in array:
        if item != None:
            if isinstance(item, list):
                flat_list += flatten(item)
            else:
                flat_list.append(item)
                
    return flat_list

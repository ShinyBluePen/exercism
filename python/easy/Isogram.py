"""Isogram

https://exercism.org/tracks/python/exercises/isogram
"""
e
def is_isogram(string: str) -> bool:
    """Determine if a given string is an isogram (word with no repeating characters).  Excludes spaces and hyphens
    
    :param string: str - String to check if is an isogram.
    :return: bool - True if `string` is an isogram.
    """
    string = string.upper().replace(" ", "").replace("-", "")
    return len(string) == len(set(string))

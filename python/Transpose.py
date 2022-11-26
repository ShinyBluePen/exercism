"""Transpose

https://exercism.org/tracks/python/exercises/transpose
"""

from itertools import zip_longest

def transpose(matrix: str) -> str:
    """Transpose a string delimited by new lines as a matrix.
    
    :param matrix: - A string delimited by newline characters "\n".
    :return: - A transposition of the given "`matrix`", still as a string.
    """
    trans = zip_longest(*matrix.splitlines(), fillvalue="·")
    return "\n".join(["".join(row).rstrip("·").replace("·", " ") for row in trans])
    

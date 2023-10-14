"""Hamming

https://exercism.org/tracks/python/exercises/hamming
"""

def distance(a: str, b: str) -> int:
    """Calculate hamming distance (# of differences) between 2 strings.
    
    :param a: str - First string.
    :param b: str - Second string.
    :return: int - Number of differences between strings `a` and `b`.`
    """
    if len(a) != len(b): raise ValueError("Strands must be of equal length.")
    return sum([1 if a != b  else 0 for a, b in zip(a.upper(), b.upper())])

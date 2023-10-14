"""Sublist

https://exercism.org/tracks/python/exercises/sublist
"""

EQUAL =     1
SUBLIST =   2
SUPERLIST = 3
UNEQUAL =   0

def sublist(l1: list[int], l2: list[int]):
    """Determine if `l1` is (un)equal to, or a sub/super-list of `l2`.
    
    :param l1: - A list of values.
    :param l2: - Another list of values.
    :return: enum - An enumerator value identifying the sublist status of `l2`.
    """
    l1s = "".join([f"-{str(c)}-" for c in l1])
    l2s = "".join([f"-{str(c)}-" for c in l2])
    
    if l1s == l2s: return EQUAL
    if l1s in l2s: return SUBLIST
    if l2s in l1s: return SUPERLIST
        
    return UNEQUAL

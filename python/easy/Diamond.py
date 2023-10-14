"""Diamond

https://exercism.org/tracks/python/exercises/diamond
"""

def row(cc: int, ext_pad: int) -> str:
    """Return a row of an alphabet "diamond".
    
    :param cc: - "Character Count".
    :param ext_pad: - The amount of padding on the sides of the row.
    :return: - A "row", such as "  C     C  ".
    """
    a = (' ' * (ext_pad - cc)) + (chr(cc + 65)) + (' ' * cc) # assemble half the row
    return a + ''.join(reversed(a[:-1]))                     # return the full row

def rows(letter: str) -> list[str]:
    """Assemble a x/y symmetrical diamond of characters from "A" to `letter`.
    
    :letter: - The given `letter` determines the size of the diamond; it's middle row.
    :return arr: - As stated.
    """
    size = ord(letter) - 64                               # length up to given `letter`
    arr = [row(i, ord(letter) - 65) for i in range(size)] # add rows until the given `letter` row
    arr.extend(arr[-2::-1])                               # add bottom half, excluding final row
    
    return arr

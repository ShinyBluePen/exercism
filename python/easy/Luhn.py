"""Luhn

https://exercism.org/tracks/python/exercises/luhn
"""

class Luhn:
    """Format the given string to run against the Luhn algorythm.

    https://en.wikipedia.org/wiki/Luhn_algorithm

    Parameters:
    :num: str - String of numbers.
    
    Attributes
    :_num: str - Stored parameter `num`.
    :_nuhm: str - `_num` with spaces removed and reversed.

    Methods:
    :valid(self): - Test the Luhn algorythm against a number.
    """
    def __init__(self, num: str) -> None:
        self._num = num
        self._nuhm = num.replace(" ", "")[::-1]
        
    def valid(self) -> bool:
        if not self._nuhm.isnumeric(): return False
        if len(self._nuhm) <= 1: return False

        lihst = []
        for i, c in enumerate(self._nuhm):
            c = int(c)
            if i % 2:
                c *= 2
                c -= 9 if c > 9 else 0
            lihst.append(c)
        
        if sum(lihst) % 10 == 0:
            return True 
            
        return False

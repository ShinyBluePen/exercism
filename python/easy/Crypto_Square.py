"""Crypto square

https://exercism.org/tracks/python/exercises/crypto-square
"""

from itertools import zip_longest
from textwrap import wrap
import math

def cipher_text(plain_text: str) -> str:
    """Encode plaintext into a crypto square.
    
    :param plaint_text: - A string to encode..
    :return: - `plain_text` encoded into a crypto square.
    """
    # normalize input
    s = "".join([c for c in plain_text.lower() if c.isalnum()])
    
    # dodge divide by zero error
    if not s: return ""

    # compute appropriate rows and columns
    p = len(s) # perimeter
    c = math.ceil(math.sqrt(p)) # columns
    r = math.ceil(p / c) # rows
    
    # transform string into a rectangular array
    s_square = wrap(s, c)
    
    # transpose array
    trans_s_square = zip_longest(*s_square, fillvalue=" ")

    return " ".join(["".join(line) for line in trans_s_square])

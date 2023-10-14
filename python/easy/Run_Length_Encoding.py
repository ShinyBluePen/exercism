"""Run-Length Encoding

https://exercism.org/tracks/python/exercises/run-length-encoding
"""

from itertools import groupby

def encode(s: str) -> str:
    """Encode a string such as `aabbbcccca` and return it as `2a3b4ca`
    
    :param s: - Any given string.
    :return: - An RTE encoded string.
    """
    groups = groupby(s)
    # grab counts of consecutive characters `(count, char)`
    sections = [(sum(1 for _ in count), char) for char, count in groups]
    return "".join(f"{(count if count > 1 else '')}{char}" for count, char in sections)

def decode(s: str) -> str:
    """Decode a string such as `2a3b4ca` and return it as `aabbbcccca`
    
    :param s: - A potentially RTE encoded string.
    :return: - An RTE decoded string.
    """
    count = ""
    decoded = ""

    for c in s:
        if c.isdigit():
            count += c
        if not count:
            decoded += c
        elif not c.isdigit():
            decoded += str(int(count) * c)
            count = ""
            
    return decoded

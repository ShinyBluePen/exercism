"""Simple Cipher

https://exercism.org/tracks/python/exercises/simple-cipher
"""

import secrets
from string import ascii_lowercase

rand_256 = ''.join(secrets.choice(ascii_lowercase) for i in range(256))

class Cipher:
    """Create a rotational cipher key and provide the methods for (de/en)cryption.

    Parameters:
    :param key: str - A desired key may be passed, else a default string of 256 characters is used.

    Attributes:
    :key: str - A string of characters whose numerical values are used to perform substitution ciphering.

    Methods:
    :encode(self, text: str, shift: int=1) -> str: - Rotate each letter in `text` using corresponding 
                                                     letters in the `Cipher` key as an ord() mask.
    :decode(self, text: str) -> str: - Decode a `text` by reversing the encryption.

    Raises:
    None
    """
    def __init__(self, key: str=rand_256) -> None:
        self.key = key

    def encode(self, text: str, shift: int=1) -> str:
        key_values = {char: val for char, val in zip(ascii_lowercase, [d for d in range(26)])}
        rotation = ""
        for i, c in enumerate(text):
            # rotational logic
            cycle = lambda char, key, scope: chr((ord(char) + shift*key_values[key] - scope) % 26 + scope)
            
            _i = i % len(self.key) # wrap key if key longer than text
            rotation += (cycle(c, self.key[_i], 65) if c.isupper() else # rotate upper case letters
                         cycle(c, self.key[_i], 97) if c.islower() else # rotate lower case letters
                         c)                                             # do NOT rotate non-letters
            
        return rotation

    def decode(self, text: str) -> str:
        return self.encode(text, shift=-1)

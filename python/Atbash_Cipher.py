"""Atbash Cipher

https://exercism.org/tracks/python/exercises/atbash-cipher
"""

from string import ascii_lowercase as abc

def encode(plain_text: str) -> str:
    """Encode plaintext with an Atbash cipher.

    https://en.wikipedia.org/wiki/Atbash
    
    :param plain_text: - A string to encode with an Atbash cipher algorhythm.
    :return: - Atbash cipher text.
    """
    cipher_text = []
    cipher_word = ""
    
    for c in plain_text:
        cipher_word += flip(c)
        if len(cipher_word) is 5 or c is plain_text[-1]:
            cipher_text.append(cipher_word)
            cipher_word = ""

    return " ".join(cipher_text).strip()

def decode(cipher_text: str) -> str:
    """Decode ciphertext encoded by an Atbash cipher.
    
    :param cipher_text: - Text encoded with an Atbash cipher.
    :return: - Plain text, but still in 5 character "words" from the cipher. One
               could implement a dictionary to rebuild the string properly, but
               that fails the Exercism tests.
    """
    return "".join([flip(c) for c in cipher_text])

def flip(char: str) -> str:
    """Flip an alphabetical character from a -> z, B -> y, c -> x, etc.
    
    Any uppercase letters will be returned flipped lowercase.  Digits are 
    returned as is, anything else is discarded.
    
    :param char: - String character to flip.
    :return: - The flipped character.
    """
    flip_table = {x: y for x, y in zip(abc, abc[::-1])}
    if char.isalpha(): return flip_table[char.lower()]
    if char.isdigit(): return char
    return ""
    

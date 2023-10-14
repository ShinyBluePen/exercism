"""Pangram

https://exercism.org/tracks/python/exercises/pangram
"""
import string

def is_pangram(sentence: str) -> bool:
    """Determine if the given `sentence` is a pangram.
    
    A pangram is a sentence using every letter of the alphabet at least once.

    :param sentence: str - Sentence to check for pangram-ness.
    :return: bool - Return True if given `sentence` is a pangram.
    """
    return set(string.ascii_uppercase).issubset(sentence.upper())

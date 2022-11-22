"""Acronym

https://exercism.org/tracks/python/exercises/acronym
"""

def abbreviate(words: str) -> str:
    """Convert a string of long words to an acronym.
    
    :param words: - A string of words.
    :return: - A string of the first uppercase letters of each word in `words`.
    """
    words = words.replace("-", " ").replace("_", " ").split()
    return "".join(word[0].upper() for word in words)
    

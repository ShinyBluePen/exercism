"""Anagram

https://exercism.org/tracks/python/exercises/anagram
"""

def find_anagrams(word: str, candidates: str) -> list[str]:
    """Find any anagrams of a word in a list of words.
    
    :param word: - The given `word` to look for anagrams of.
    :param candidates: - A string of potential anagrams for the given `word`.
    :return: -A list of all anagrams of `word` found within `candidates`.
    """
    return [w for w in candidates
           if w.upper() != word.upper()
           if sorted(w.upper()) == sorted(word.upper())]

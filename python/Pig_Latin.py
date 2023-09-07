"""Pig Latin

https://exercism.org/tracks/python/exercises/pig-latin
"""

VOWELS = "AEIOUY"

def translate(text: str) -> str:
    """Return a string translated into pig-latin.

    https://en.wikipedia.org/wiki/Pig_latin

    :param text: - String to translate into Pig Latin.
    :return: - `text` translated into Pig Latin.
    """
    return " ".join([oink(word) for word in text.split()])

def oink(word: str) -> str:
    """Translate a single word into Pig Latin."""
    w = word.upper()
    
    # check special clusters
    if w.startswith("XR") or w.startswith("YT"):
        return f"{word}ay"
        
    # vowel words
    if w[0] in VOWELS:
        # check for "y" as consonant
        if w.startswith("Y"):
            return f"{word[1:]}yay"
            
        return f"{word}ay"
        
    # consonant and consonant cluster words
    cluster = ""
    for i, c in enumerate(w):
        # check for vowels and the "qu" special cluster
        if c not in VOWELS or w[i-1:i+1] == "QU":
            cluster += word[i]
        else:
            break 
            
    return f"{word[len(cluster):]}{cluster}ay"

"""Pig Latin

https://exercism.org/tracks/python/exercises/pig-latin
"""

def translate(text: str) -> str:
    """Return a string translated into pig-latin.

    https://en.wikipedia.org/wiki/Pig_latin

    :param text: - String to translate into Pig Latin.
    :return: - `text` translated into Pig Latin.
    """
    vowels = list("AEIOUY")

    def oink(word: str) -> str:
        """Translate a single word into Pig Latin."""
        w = word.upper()
        
        # check special clusters
        if w[0] is "Y" and w[1] is not "T": # check for 'y' as consonant
            return word[1:] + "yay"
        if w.startswith("XR"): # check for 'xr'
            return word + "ay"
            
        # vowel words
        if w[0] in vowels:
            return word + "ay"
            
        # consonant and consonant cluster words
        cluster = ""
        for i, c in enumerate(w):
            if (c not in vowels 
                or (w[i-1] is "Q" and w[i] is "U") # check for 'qu' special cluster
                ):
                cluster += word[i]
            if c in vowels:
                break # Finished building the cluster
                
        return word[len(cluster):] + cluster + "ay"

    return " ".join([oink(word) for word in text.split()])

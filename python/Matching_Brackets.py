"""Matching Brackets

https://exercism.org/tracks/python/exercises/matching-brackets
"""

def is_paired(s: str) -> bool:
    """Verify that any open [], (), or {} brackets close and are properly nested.
    
    :param s: - A string possibly containing brackets.
    :return: - True if all (if any) opened brackets close and are properly nested.
    """
    s_brackets = "".join([c for c in s if c in "[](){}"])
    pairs = ["[]", "()", "{}"]
    
    for p in pairs:
        if p in s_brackets:
            return is_paired(s_brackets.replace(p, ""))

    return not s_brackets

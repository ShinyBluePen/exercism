"""ISBN Verifier

https://exercism.org/tracks/python/exercises/isbn-verifier
"""

def is_valid(isbn: str) -> bool:
    """Determine if a given string is a valid ISBN.
    
    :param isbn: - Potential ISBN.
    :return: - True if the given `isbn` is valid.
    """
    d = list(isbn.replace("-", ""))
    
    if len(d) is 10:
        if d[-1] is "X": 
            d[-1] = "10"

        if not "".join(d).isnumeric(): 
            return False
            
        d = [int(i) for i in d]
        return not sum(int(x)*y for x, y in zip(d, range(10, 0, -1))) % 11

    return False # ISBN is > or < 10 digits in length

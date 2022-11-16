"""Two Fer

https://exercism.org/tracks/python/exercises/two-fer
"""

def two_fer(name: str="you") -> str:
    """Return a simple string in the form {"One for {name}, one for me."}.

    :param name: str - The name you want to appear in the string.
    :return: str
    """
    return f"One for {name}, one for me."

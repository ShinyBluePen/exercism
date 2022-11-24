"""Series

https://exercism.org/tracks/python/exercises/series
"""

def slices(series: str, length: int) -> list[str]:
    """Return all `length`s of contiguous digits from a `series`.

    For example, the string "49142" has the following 3-digit series:
        "491"
        "914"
        "142"
    And the following 4-digit series:
        "4914"
        "9142"
    
    :param series: - A string of integers.
    :param length: - The `length` slices of the `series` should be in.
    :return: - A list of string slices.
    """
    check_errors(series, length)
    return [series[i:i + length] for i in range(len(series) - length + 1)]

def check_errors(series: str, length: int) -> None:
    """Error check a series slicing function."""
    if not series: raise ValueError("series cannot be empty")
    if not length: raise ValueError("slice length cannot be zero")
    if length < 0: raise ValueError("slice length cannot be negative")
    if len(series) < length: raise ValueError("slice length cannot be greater than series length")

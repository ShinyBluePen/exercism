"""Leap

https://exercism.org/tracks/python/exercises/leap
"""

def leap_year(year: int) -> bool:
    """Return True if the given year is a leap year.
    
    :param year: int - given year to check.
    :return bool: - True if the given year is a leap year.
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

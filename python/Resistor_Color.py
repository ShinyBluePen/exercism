"""Resistor Color

https://exercism.org/tracks/python/exercises/resistor-color
"""

_COLORS = "black brown red orange yellow green blue violet grey white".split()
COLOR_CODES = {color: code for color, code in zip(_COLORS, range(len(_COLORS)))}

def color_code(color: str) -> str:
    """Return the code of the given `color`.

    :param color: str - Given color to find the code for.
    """
    return COLOR_CODES[color]

def colors() -> list[str]:
    """Return a list of all the colors.
    
    :return: list[str] - List of all current coded colors."""
    return list(COLOR_CODES)
    

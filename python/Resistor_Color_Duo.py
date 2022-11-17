"""Resistor Color Duo

https://exercism.org/tracks/python/exercises/resistor-color-duo
"""

_colors = "black brown red orange yellow green blue violet grey white".split()
COLORS = {color: str(code) for color, code in zip(_colors, range(len(_colors)))}

def value(colors: list[str]) -> int:
    """Add the first two colors from a given list to return an int resistance value.
    
    :param colors: list[str] - List of resistance bands to sum.
    :return: int - The resistance value of the combined color bands.
    """
    # first, second, *_ = colors # unpacking offers a cool solution if we want/need to use names
    return int(COLORS[colors[0]] + COLORS[colors[1]])

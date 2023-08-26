"""Resistor Color Trio

https://exercism.org/tracks/python/exercises/resistor-color-trio
"""

def label(colors: list[str]) -> str:
    """Decode the resistance value in ohms from the coloured bands present on a resistor.
    
    :param colors: - List of resistance bands to sum.
    :return: - The resistance value in Ohms of the combined color bands.
    """
    _clrs = "black brown red orange yellow green blue violet grey white".split()
    R_CODES = {color: str(code) for color, code in zip(_clrs, range(len(_clrs)))}
    SCALES = {1: "ohms", 1e3: "kiloohms", 1e6: "megaohms", 1e9: "gigaohms"}

    first, second, ohms, *_ = colors
    measure = int(f"{int(R_CODES[first] + R_CODES[second])}{int(R_CODES[ohms]) * '0'}")

    if measure == 0: # x3 black bands
        return "0 ohms"

    for scale in reversed(SCALES):
        if measure >= scale:
            measure //= scale
            magnitude = SCALES[scale]
            break

    # get key by value
    # measure = measure // [i for i in SCALES if SCALES[i] == magnitude][0] 

    return f"{int(measure)} {magnitude}"

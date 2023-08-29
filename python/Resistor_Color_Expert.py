"""Resistor Color Expert
 
https://exercism.org/tracks/python/exercises/resistor-color-expert
"""

def resistor_label(colors):
    """Decode the resistance and tolerance values of resistors based on their color bands.
    
    :param colors: list[str] - List of resistance bands representing resistence and tolerance values.
    :return: str - The resistance value in Ohms of the combined color bands.
    """
    _r_clrs = "black brown red orange yellow green blue violet grey white".split()
    R_CODES = {color: str(code) for color, code in zip(_r_clrs, range(len(_r_clrs)))}
    T_CODES = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10,}
    SCALES = {1e12: "teraohms", 1e9: "gigaohms", 1e6: "megaohms", 1e3: "kiloohms", 1: "ohms",}
    
    if len(colors) == 1:
        return f"{R_CODES[colors[0]]} ohms"
    
    *bands, multiplier, tolerance = colors

    # get measure of resistance
    digit_band_values = [R_CODES[band] for band in bands]
    digit_band_values.append(int(R_CODES[multiplier]) * "0") # append {multiplier} of 0's
    
    measure = int("".join(digit_band_values))

    # determine appropriate `scale`, apply to `measure`, and return
    for degree, unit in SCALES.items():
        if measure >= degree:
            measure /= degree
            scale = unit
            return f"{measure:g} {scale} ±{T_CODES[tolerance]}%"

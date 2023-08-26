"""Resistor Color Expert
 
https://exercism.org/tracks/python/exercises/resistor-color-expert
"""

def resistor_label(colors: list[str]) -> str:
    """Decode the resistance and tolerance values of resistors based on their color bands.
    
    :param colors: - List of resistance bands representing resistence and tolerance values.
    :return: - The resistance value in Ohms of the combined color bands.
    """
    _r_clrs = "black brown red orange yellow green blue violet grey white".split()
    R_CODES = {color: str(code) for color, code in zip(_r_clrs, range(len(_r_clrs)))}
    T_CODES = {"grey": 0.05,
               "violet": 0.1,
               "blue": 0.25,
               "green": 0.5,
               "brown": 1,
               "red": 2,
               "gold": 5,
               "silver": 10,}
    SCALES = {1e12: "teraohms",
              1e9: "gigaohms",
              1e6: "megaohms",
              1e3: "kiloohms",
              1: "ohms",}
    
    if len(colors) == 1:
        return f"{R_CODES[colors[0]]} ohms"
    
    *bands, magnitude, tolerance = colors

    # get measure of resistance
    digit_band_values = [R_CODES[band] for band in bands]
    digit_band_values.append(int(R_CODES[magnitude]) * "0") # append {magnitude} of 0's
    
    measure = int("".join(digit_band_values))

    # determine appropriate unit
    for degree, unit in SCALES.items():
        if measure >= degree:
            measure /= degree
            scale = unit
            break

    # handle unwanted floats
    if str(measure)[-1] == "0": # decimal values don't have trailing 0's. This catches
        measure = int(measure)  #   numbers that should be ints, such as 2.0, 13.0, etc
        
    return f"{measure} {scale} ±{T_CODES[tolerance]}%"

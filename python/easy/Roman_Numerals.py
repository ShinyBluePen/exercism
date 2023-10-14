"""Roman Numerals

https://exercism.org/tracks/python/exercises/roman-numerals

I particularly liked @jeffdparker's
https://exercism.org/tracks/python/exercises/roman-numerals/solutions/jeffdparker

and @glennj's solutions
https://exercism.org/tracks/python/exercises/roman-numerals/solutions/glennj
"""

def roman(num: int) -> str:
    """Convert a base 10 integer less than 4,000 to Roman numerals.
    
    :param num: - An integer.
    :return conv: - The Roman Numeral conversion of `num`.
    """
    num_digits = [int(d) for d in str(num)]

    pos = len(num_digits)
    for i, d in enumerate(num_digits):
        if pos is 4:
            num_digits[i] = "M" * d
        if pos is 3:
            if d < 5: num_digits[i] = "C" * d
            else:     num_digits[i] = "D" + ("C" * (d-5))
        if pos is 2:
            if d < 5: num_digits[i] = "X" * d
            else:     num_digits[i] = "L" + ("X" * (d-5))
        if pos is 1:
            if d < 5: num_digits[i] = "I" * d
            else:     num_digits[i] = "V" + ("I" * (d-5))
        pos -= 1
        
    conv = "".join(num_digits)
    conv = (conv.replace("VIIII", "IX").replace("IIII", "IV")
                .replace("LXXXX", "XC").replace("XXXX", "XL")
                .replace("DCCCC", "CM").replace("CCCC", "CD"))
    
    return conv
    

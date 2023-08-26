"""All Your Base

https://exercism.org/tracks/python/exercises/all-your-base
"""

def rebase(input_base: int, digits: list[int], output_base: int):
    """Convert a number from one one base to another base.

    :param input_base: - The input base of the number given in `digits`.
    :param digits: - The number to convert to `output_base`.
    :param output_base: - The target base to convert the number given by `digits` to.
    :return rebased | [0]: - The number given by `digits` rebased to `output_base`.
    """
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")
    for digit in digits:
        if 0 > digit or digit > input_base-1: # bases start at 0
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # convert to decimal through positional notation
    decimal = sum(pow(input_base, i) * d for i, d in enumerate(reversed(digits)))
        
    # convert to any other base from decimal
    rebased = []
    while decimal:
        decimal, remainder = divmod(decimal, output_base)
        rebased.append(remainder)

    return rebased[::-1] or [0]
    

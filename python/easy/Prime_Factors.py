"""Prime Factors

https://exercism.org/tracks/python/exercises/prime-factors
"""

def factors(value: int) -> list[int]:
    """Determine the prime factors of a given number.
    
    :param value: - An integer to determine the prime facotrs of.
    :return: - A list of the prime factors of `value`.
    """
    prime_factors = []
    factor = 2
    while value > 1:
        if not value % factor:
            prime_factors.append(factor)
            value /= factor
        else:
            factor += 1
    return prime_factors

"""Perfect Numbers

https://exercism.org/tracks/python/exercises/perfect-numbers
"""

def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: - A positive integer.
    :return result: - The classification of the input integer.
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    factors = [f for f in range(1, number) if not number % f]

    if   sum(factors) == number: result = "perfect"
    elif sum(factors) >  number: result = "abundant"
    else:                        result = "deficient"
    
    return result

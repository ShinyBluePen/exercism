"""Sieve (of Eratosthenes)

https://exercism.org/tracks/python/exercises/sieve/
"""

def primes(limit: int) -> list[int, ...]:
    """Find all prime numbers up to and including the given `limit`.
    
    :param limit: int - Inclusive range of numbers to search for primes.
    :return list[int] - List of all prime numbers up to the given limit.
    """        
    domain = [[i, True] for i in range(limit+1)]
    domain[0], domain[1] = (0, False), (1, False)

    primes = []
    for digit, flag in domain:
        if flag:
            primes.append(digit)
            # update all flags in domain for multiples of digit
            for i in range(digit, len(domain), digit):
                domain[i] = [i, False]

    return primes

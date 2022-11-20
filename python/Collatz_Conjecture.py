"""Collatz Conjecture

https://exercism.org/tracks/python/exercises/collatz-conjecture
"""

def steps(number: int) -> int:
    """Count collatz steps for a given number.

    :param number: - The number to begin Collatzing.
    :return steps: - Collatz steps from `number` to 1.
    
    The Collatz Conjecture or 3x+1 problem can be summarized as follows:
        Take any positive integer n. If n is even, divide n by 2 to get n / 2.
        If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the
        process indefinitely. The conjecture states that no matter which
        number you start with, you will always reach 1 eventually.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        if not number % 2: # even number
            number /= 2
        else:              # odd number
            number *= 3
            number += 1
        steps += 1

    return steps
  

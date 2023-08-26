"""Pythagorean Triplet

https://exercism.org/tracks/python/exercises/pythagorean-triplet/

Credit to @charles-wangkai
https://exercism.org/tracks/python/exercises/pythagorean-triplet/solutions/charles-wangkai
"""

def triplets_with_sum(n: int) -> list[list[int]]:
    """Given `n`, find all Pythagorean triplets for which a + b + c = n.

    A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which:
        a² + b² = c²
        a < b < c
    for ex:
        3² + 4² = 5²
    
    :param n: - A total sum of some theoretical P. triplet sets.
    :return: - All sets of P. triplets which total `n`.
    """
    result = []
    for a in range(1, (n // 3) + 1):
        for b in range(a, ((n - a) // 2) + 1):
            c = n - a - b
            if (a * a) + (b * b) == (c * c):
                result.append([a, b, c])
    return result

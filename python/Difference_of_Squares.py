"""Difference of Squares

https://exercism.org/tracks/python/exercises/difference-of-squares
"""

def square_of_sum(number: int) -> int:
    """Square of the sum of the first `number` of natural numbers."""
    return sum(range(1, number+1)) ** 2
        
def sum_of_squares(number: int) -> int:
    """Sum of the squares of the first `number` of natural numbers."""
    return sum((n ** 2 for n in range(1, number+1)))

def difference_of_squares(number: int) -> int:
    """Difference between the square of the sum and the sum of the squares of the first `number` of natural numbers."""
    return square_of_sum(number) - sum_of_squares(number)

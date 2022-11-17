""""Grains

https://exercism.org/tracks/python/exercises/grains
"""

def square(number: int) -> int:
    """Return the amount of rice on a given square from the board.
    
    :param number: int - The consequetive square of the chessboard.
    :return int: - The number of rice grains on the given `number` square.
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)

def total() -> int:
    """Return the total of all grains of rice on a chessboard where the 
    grains double on each successive square.
    
    :return int: - All rice grains."""
    return (1 << 64) - 1

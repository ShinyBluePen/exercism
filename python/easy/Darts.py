"""Darts

https://exercism.org/tracks/python/exercises/darts
"""

def score(x: int, y: int) -> int:
    """Return the score of a thrown dart based on its position on a circular board.
    
    :param x: int - Dart's X position.
    :param y: int - Dart's Y position.
    :return: int - Score determined from the darts (`x`, `y`) position on the board.
    """
    # Darts' position relative to the radii of the concentrentric circles of the board
    r = (x**2 + y**2)**0.5
    
    if r <= 1:
        return 10
    if r <= 5:
        return 5
    if  r <= 10:
        return 1
        
    return 0 # missed the board

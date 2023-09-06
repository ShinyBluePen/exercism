"""Spiral Matrix
 
https://exercism.org/tracks/python/exercises/spiral-matrix
"""
from itertools import cycle

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # Right, Down, Left, Up

def spiral_matrix(size: int) -> list[list[int]]:
    """return a NxN square matrix of numbers 1...N^2 in spiral order.
 
    The matrix should be filled with natural numbers, starting from 1 in 
    the top-left corner, increasing in an inward, clockwise spiral order.
    
    :param size: - The length x width size of the matrix.
    :return: - The matrix, as specified.
    """
    matrix = [[0] * size for row in range(size)]
    directions = cycle(DIRECTIONS)
    
    x, y, dx, dy = 0, 0, *next(directions)
    for value in range(1, size**2+1):
        matrix[x][y] = value
        
        # Check if the next position is valid, if it's not, change direction
        valid = lambda coord: 0 <= coord < size
        if not valid(x + dx) or not valid(y + dy) or matrix[x + dx][y + dy]:
            dx, dy = next(directions)

        x += dx
        y += dy
        
    return matrix
    

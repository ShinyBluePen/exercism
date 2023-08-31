"""Spiral Matrix

https://exercism.org/tracks/python/exercises/spiral-matrix
"""

def spiral_matrix(size: int) -> list[list[int]]:
    """return a NxN square matrix of numbers 1...N^2 in spiral order.

    The matrix should be filled with natural numbers, starting from 1 in 
    the top-left corner, increasing in an inward, clockwise spiral order.
    
    :param size: - The length x width size of the matrix.
    :return: - The matrix, as specified.
    """
    matrix = [[0] * size for row in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    d, x, y = 0, 0, 0
    for slot in range(1, size*size+1):
        matrix[x][y] = slot
        
        next_x = x + directions[d][0]
        next_y = y + directions[d][1]
        
        # Check if the next position is valid
        if (0 <= next_x < size and 
            0 <= next_y < size and 
            not matrix[next_x][next_y]
        ):
            x, y = next_x, next_y
        # Change direction if the next position is invalid
        else:
            d = (d + 1) % 4
            x += directions[d][0]
            y += directions[d][1]

    return matrix

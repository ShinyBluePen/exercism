"""Pascals Triangle

https://exercism.org/tracks/python/exercises/pascals-triangle
"""

def rows(max_depth: int, previous_row: list[int]=[1]) -> list[list[int]]:
    """Compute Pascal's triangle up to a given number of rows.

    In Pascal's Triangle each number is computed by adding the numbers 
    to the right and left of the current position in the previous row.
    for ex:

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    
    :param max_depth: - The target depth of rows for the triangle.
    :param previous_row: - The last row built.
    :return: - The fully assembled "triangle".
    """
    if max_depth < 0: 
        raise ValueError("number of rows is negative")
    if max_depth == 0: 
        return []

    get_item = lambda i: previous_row[i] if 0 <= i < len(previous_row) else 0
    next_row = [get_item(i-1) + get_item(i) for i in range(len(previous_row) + 1)]

    return [previous_row] + rows(max_depth - 1, next_row)
    

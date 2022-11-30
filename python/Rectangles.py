"""Rectangles

https://exercism.org/tracks/python/exercises/rectangles

Credit to @baltic-tea
I cleaned it up a bit and added comments to easily track what was happening on each line.
https://exercism.org/tracks/python/exercises/rectangles/solutions/baltic-tea
"""

def rectangles(strings: list[str]) -> int:
    """Count # of rectangles present in an ASCII diagram given as a matrix of strings.
    
    :param strings: list[str] - a matrix of an arbitrary number of strings of equal length.
    :return count: int - the total number of rectangles present in the given matrix.
    """
    count = 0
    # for row in matrix
    for pivot, row in enumerate(strings):
        length = len(row)
        width = len(strings)
        # for col in row
        for col in range(length): 
            # top left vertex of a rectangle
            if row[col] == '+':
                # look for top right vertex in the same row as top left vertex
                for row_item in range(col + 1, length): 
                    # top right vertex of a rectangle
                    if row[row_item] == '+':
                        # check the columns of the top L and R verticies for closing bottom verticies
                        for col_item in range(pivot + 1, width): 
                            # bottom left and right verticies
                            if (strings[col_item][col] == '+' and 
                                strings[col_item][row_item] == '+'): 
                                count += 1
                            # rectangle is not complete vertically
                            elif (strings[col_item][col] not in '|+' or 
                                  strings[col_item][row_item] not in '|+'): 
                                break
                    # rectangle is not complete horizontally
                    elif row[row_item] != '-': 
                        break
    return count

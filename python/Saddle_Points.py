"""Saddle Points

https://exercism.org/tracks/python/exercises/saddle-points
"""

def saddle_points(matrix: list[list[int]]) -> list[dict]:
    """Detect saddle points in a matrix.
    
    A "saddle point" is greater than or equal to every element in its 
    row and less than or equal to every element in its column.

    :param matrix: - Representated as a list of lists of ints.
    :return saddle_points: - A dict specifying the row/column of all present saddle points.
    """
    columns = [list(c) for c in zip(*matrix)]
    
    saddle_points = []
    for ri, row in enumerate(matrix):
        if len(row) != len(matrix[0]): 
            raise ValueError("irregular matrix")
        row_max = max(row)        
        for ci, col in enumerate(columns):
            col_min = min(col)        
            if row_max is col_min:
                saddle_points.append({"row": ri+1, "column": ci+1})
            
    return saddle_points

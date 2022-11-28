"""Matrix

https://exercism.org/tracks/python/exercises/matrix
"""

class Matrix:
    """Initialize a matrix object from a given matrix-like string.

    Parameters:
    :param matrix_string: str - A string delimited by newline characters; "\n".

    Attributes:
    :rows: - .
    :columns: - .

    Methods:
    :row(self, index): - Return a row list from the matrix.
    :column(self, index): - Return a column list from the matrix.

    Raises:
    None
    """
    def __init__(self, matrix_string: list[str]):
        self.rows = [[int(i) for i in row.split()] for row in matrix_string.splitlines()]
        self.columns = [list(col) for col in zip(*self.rows)]
            
    def row(self, index: int) -> list[str]:
        return self.rows[index-1]

    def column(self, index: int) -> list[str]:
        return self.columns[index-1]

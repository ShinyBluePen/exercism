"""Queen Attack

https://exercism.org/tracks/python/exercises/queen-attack
"""

class Queen:
    """A piece in the game of Chess.
    
    https://en.wikipedia.org/wiki/Chess
    
    Parameters:
    :param row: int - Queens initial vertical position.
    :param col: int - Queens initial horizontal position.
    
    Attributes:
    :_row: int - Queens current vertical position.
    :_col: int - Queens current horizontal position.
    
    Methods:
    :check_position(self): - Checks to make sure Queen is placed on the board when created.
    :can_attack(self, other_queen): - Determine if a queen can attack another queen.
    
    Raises:
    :ValueError: - If the queens positioning is invalid.
    """
    def __init__(self, row: int, col: int):
        self._row = row
        self._col = col
        self.check_position()

    def can_attack(self, other_queen):
        if self._row == other_queen._row and self._col == other_queen._col:
            raise ValueError("Invalid queen position: both queens in the same square")

        r = abs(self._row - other_queen._row) # horizontal
        c = abs(self._col - other_queen._col) # vertical
        return r == 0 or c == 0 or r == c     # diagonal

    def check_position(self):
        "Ensure given coordinates are a valid square on a chess board."
        if self._row < 0: raise ValueError("row not positive")
        if self._row > 7: raise ValueError("row not on board")
        if self._col < 0: raise ValueError("column not positive")
        if self._col > 7: raise ValueError("column not on board")
            

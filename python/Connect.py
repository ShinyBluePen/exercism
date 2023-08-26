"""Connect

https://exercism.org/tracks/python/exercises/connect

Credit to @AlexPark
https://exercism.org/tracks/python/exercises/connect/solutions/AlexPark
"""

class ConnectGame:
    """A Connect game board.

    Parameters:
    :board: str - A string representation of the Connect game board where 
                  'X' and 'O' represent players and ' ' represents empty spaces.
    
    Attributes:
    :board: str - A string representation of the Connect game board.
    
    Methods:
    :get_winner(): Return the winning player ('X' or 'O') if there is one, 
                   or an empty string if there is no winner.
    
    Raises:
    None
    """
    def __init__(self, board):
        self.board = board.replace(" ", "").split("\n")
        
    def get_winner(self):
        visited = set()
        to_visit = []
        neighbors = [(-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1)]

        # visit each item in the starting row
        for row in range(len(self.board)):
            to_visit.append((0, row, "X"))

        # visit each item in the starting column
        for col in range(len(self.board[0])):
            to_visit.append((col, 0, "O"))

        # perform an exhaustive search of the board using a FIFO stack
        while to_visit:
            tup = to_visit.pop(0)
            
            if tup in visited:
                continue
                
            visited.add(tup)
            x, y, player = tup

            # prevent index out of range errors
            if y < 0 or y >= len(self.board):
                continue
            if x < 0 or x >= len(self.board[y]):
                continue

            # empty tile
            if self.board[y][x] != player:
                continue

            # return the winning player, if any
            if player == "X" and x == len(self.board[0]) - 1:
                return player
            elif player == "O" and y == len(self.board) - 1:
                return player

            # check each tiles neighbors
            for dx, dy in neighbors:
                to_visit.append((x + dx, y + dy, player))
                
        return ""

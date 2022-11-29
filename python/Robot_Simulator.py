"""Robot Simulator

https://exercism.org/tracks/python/exercises/robot-simulator

credit to @BethanyG for an excellent solution from which I stole a lot because 
the `self.instructions` property was just so hot I had to have it.
the `moves` variable in `advance()` was also really nice.
https://exercism.org/tracks/python/exercises/robot-simulator/solutions/BethanyG
"""

NORTH, EAST, SOUTH, WEST = 0, 90, 180, 270

class Robot:
    """Representation of a robot which can turn left, right, or go forward.
    
    Coordinates increase towards North and East.

    Parameters:
    :param direction: int - The robots initial direction.
    :param x: int - The robots initial X position.
    :param y: int - The robots initial Y position.

    Attributes:
    :direction: int - The robots current direction.
    :_x: int - The robots current Y position.
    :_y: int - The robots current Y position.
    :_instructions: dict[str, func] - Instructions the robot can receive regarding it's movement.
    :coordinates: tuple[int, int] - The robots current X and Y position.

    Methods:
    :advance(self) -> None: - Moves the robot forward.
    :turn_left(self) -> None: - Changes the robots direction to the left.
    :turn_right(self) -> None: - Changes the robots direction to the right.
    :move(self, path: str) -> None: - Move robot either left, right or forward.

    Raises:
    :ValueError: - If given an invalid movement command, ex: not 'A', 'L', or 'R'.
    """
    def __init__(self, direction: int=NORTH, x: int=0, y: int=0):
        self.direction = direction
        self._x = x
        self._y = y
        self._instructions = {"A": self.advance,
                              "L": self.turn_left,
                              "R": self.turn_right}

    @property
    def coordinates(self) -> tuple[int, int]:
        return (self._x, self._y)

    def advance(self) -> None:
        moves = {NORTH: 1, SOUTH: -1, EAST: 1, WEST: -1}
        
        if self.direction in (NORTH, SOUTH):
            self._y += moves[self.direction]
        if self.direction in (EAST, WEST):
            self._x += moves[self.direction]
            
    def turn_left(self) -> None:
        self.direction = (self.direction -90) % 360
        
    def turn_right(self) -> None:
        self.direction = (self.direction + 90) % 360
        
    def move(self, path: str) -> None:
        for movement in path.upper():
            if movement not in self._instructions:
                raise ValueError("Movement commands may only be 'A', 'L', or 'R'.")
            self._instructions[movement]()

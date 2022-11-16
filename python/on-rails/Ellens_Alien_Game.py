"""Ellen's Alien Game

https://exercism.org/tracks/python/exercises/ellens-alien-game
"""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x, y):
        self.health = 3
        self.x_coordinate = x
        self.y_coordinate = y

        Alien.total_aliens_created += 1

    def hit(self) -> None:
      """Decrement Alien health by one point."""
        self.health -= 1
        
        if self.health < 0:
            self.health = 0

    def is_alive(self) -> bool:
      """Return a boolean for if Alien is alive (if health is > 0).
      
      :return: bool
      """
        return self.health != 0

    def teleport(self, x: int, y: int) -> None:
      """Move Alien object to new coordinates.
      
      :param x: int - Aliens X coordinate location.
      :param y: int - Aliens Y coordinate location.
      """
        self.x_coordinate = x
        self.y_coordinate = y

    # TODO
    def collision_detection(self, other: object) -> bool:
      """Return a boolean if an Alien is colliding with another object.
      
      :param other: object - Any other object with cordinates.
      """
        return ((self.x_coordinate == other.x_coordinate) and 
                (self.y_coordinate == other.y_coordinate))

def new_aliens_collection(many_locations: list[tuple]) -> list[tuple]:
  """Create and return a list of aliens spawned at given coordinates.
  
  :param many_locations: list[tuple] - List of alien locations where each Alien will be spawned.
  :return aliens list[tuple] - List of Alien objects whose coordinates match those given in `many_locations`.
  """
    aliens = []
    
    for location in many_locations:
        aliens.append(Alien(location[0], location[1]))

    return aliens

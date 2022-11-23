"""Robot Name

https://exercism.org/tracks/python/exercises/robot-name
"""

import random
import string

robots = []

class Robot:
    """Representation of a robot.

    Attributes:
    :name: str - The robots name, as produced by `make_name`.

    Methods:
    :make_name(self): - Generate a name for a `Robot` that starts with 2 
                        uppercase characters and ends with 3 ints.  Then
                        add the robot to `robots`.
    :reset(self): - Remove the `Robot`s name from `robots` and call `make_name`.
    """
    def __init__(self) -> None:
        self.name = self.make_name()

    def make_name(self) -> str:
        random.seed()
        chars = random.choices(string.ascii_uppercase, k = 2)
        nums = random.choices(string.digits, k = 3)
        self.name = "".join(chars + nums)
        # ensure no duplicate robot names are created
        if self.name in robots:
            self.make_name()
        robots.append(self.name)
        return self.name

    def reset(self) -> str:
        robots.remove(self.name)
        return self.make_name()

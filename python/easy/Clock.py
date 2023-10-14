"""Clock

https://exercism.org/tracks/python/exercises/clock
"""

class Clock:
    """A representation of a simple clock.

    Parameters:
    :param hours: int - The initial hours of the clock.
    :param minutes: int - The initial minutes of the clock.

    Attributes:
    :hours: int - The current hours of the clock.
    :minutes: int - The current minutes of the clock.

    Methods:
    None

    Raises:
    None
    """
    def __init__(self, hours: int, minutes: int) -> None:
        raw_mins = hours * 60 + minutes
        self.hours = raw_mins // 60 % 24
        self.minutes = raw_mins % 60
        # could also do:
        # self.minutes = (minute + hour * 60) % 1440
        
    def __repr__(self) -> str:
        return f"Clock({self.hours}, {self.minutes})"
        
    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}"
        
    def __eq__(self, other) -> bool:
        return (self.hours == other.hours) and (self.minutes == other.minutes)
        
    def __add__(self, minutes: int) -> "Clock":
        return Clock(self.hours, self.minutes + minutes)
        
    def __sub__(self, minutes:int) -> "Clock":
        return Clock(self.hours, self.minutes - minutes)
        # We could also use addition because we have already defined __add__
        # return self + (-minutes)

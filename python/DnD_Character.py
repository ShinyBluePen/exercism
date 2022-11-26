"""DnD Character

https://exercism.org/tracks/python/exercises/dnd-character
"""

import random

class Character:
    """A reprisentation of a D&D character.

    https://en.wikipedia.org/wiki/Dungeons_%26_Dragons
    
    Parameters:
    None
    
    Attributes:
    :strength: ----- .
    :dexterity: ---- .
    :constitution: - .
    :intelligence: - .
    :wisdom: ------- .
    :charisma: ----- .
    :hitpoints: ---- .
    
    Methods:
    :ability(self): - Randomly roll an attribute value.
    
    Raises:
    None
    """
    def __init__(self):
        attributes = "strength dexterity constitution intelligence wisdom charisma".split()
        
        for attr in attributes:
            setattr(self, attr, self.ability())
        
        self.hitpoints = 10 + ((self.constitution - 10) // 2)
        
    def ability(self) -> int:
        """Roll 3 d4 and return a list of the 3 highest rolled dice values."""
        return sum(sorted(roll(num=4))[1:])

def roll(faces: int=6, num: int=1) -> list[int]:
    """Roll any number of die of a specified face.
    
    :param faces: - The number of faces on each die.
    :param num: - The number of dice to roll.
    :return: - A list of the specified dice randomly rolled.
    """
    return [random.randint(1, faces) for d in range(num)]

def modifier(attr: int) -> int:
    """Determine atribute modifier."""
    return (attr - 10) // 2

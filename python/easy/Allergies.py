"""Allergies

https://exercism.org/tracks/python/exercises/allergies
"""

class Allergies:
    """Given a person's allergy score, determine whether or not 
    they're allergic to a given item, and their full list of allergies.

    Parameters:
    :param score: int - An individuals allergen score.  Higher == more allergens.

    Attributes:
    :score: int - An individuals allergen score.  Higher == more allergens.
    :allergy_list: list[str] - A list of all allergens a person suffers from.
    :lst: list[str] - Returns `allergy_list`.

    Methods:
    :allergic_to(self, item): - True if person is allergic to the given `item`.

    Raises:
    None
    """
    ALLERGENS = {
    "eggs":         1,
    "peanuts":      2,
    "shellfish":    4,
    "strawberries": 8,
    "tomatoes":     16,
    "chocolate":    32,
    "pollen":       64,
    "cats":         128,
    }

    def __init__(self, score: int):
        self.score = score
        self.allergy_list = [allergy for (allergy, score) 
                             in self.ALLERGENS.items() 
                             if self.score & score != 0]

    def allergic_to(self, item: str) -> bool:
        return item in self.allergy_list

    @property
    def lst(self) -> list[str]:
        return self.allergy_list
        

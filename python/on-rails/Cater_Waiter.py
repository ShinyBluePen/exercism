"""Cater Waiter

https://exercism.org/tracks/python/exercises/cater-waiter
"""

from sets_categories_data import *

def clean_ingredients(dish_name: str, dish_ingredients: str) -> tuple[str, set[str]]:
    """

    :param dish_name: str - .
    :param dish_ingredients: list[str] - .
    :return: tuple[str, set[str]] - Tuple of (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    return dish_name, set(dish_ingredients)

def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    """

    :param drink_name: str - .
    :param drink_ingredients: list[str] - .
    :return: str - drink name + ("Mocktail" or "Cocktail").

    The function should return the name of the drink followed by "Mocktail" if the drink 
    has no alcoholic ingredients, and drink name followed by "Cocktail" if the drink 
    includes alcohol.
    """
    if ALCOHOLS.intersection(drink_ingredients):
        return f"{drink_name} Cocktail"
        
    return f"{drink_name} Mocktail"

def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    """

    :param dish_name: str - .
    :param dish_ingredients: list[str] - .
    :return: str - "dish name: CATEGORY".

    This function should return a string with the `dish name: <CATEGORY>` 
    (which meal category the dish belongs to).  All dishes will "fit" into one of the 
    categories imported from `sets_categories_data.py` (VEGAN, VEGETARIAN, PALEO, KETO, 
    or OMNIVORE).
    """
    categories = {"VEGAN": VEGAN, 
                  "VEGETARIAN": VEGETARIAN, 
                  "PALEO": PALEO, 
                  "KETO": KETO, 
                  "OMNIVORE": OMNIVORE
    }
    
    for key, value in categories.items():
        if set(dish_ingredients).issubset(value):
            category = key

    return f"{dish_name}: {category}"

def tag_special_ingredients(dish: tuple[str, list[str]]) -> tuple[str, set[str]]:
    """

    :param dish: tuple[str, list[str]] - Tuple of (str of dish name, list of dish ingredients).
    :return: tuple[str, set[str]] - Tuple of (str of dish name, set of dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special 
    note on the dish description.  For the purposes of this exercise, all allergens 
    or special ingredients that need to be tracked are in the SPECIAL_INGREDIENTS 
    constant imported from `sets_categories_data.py`.
    """
    dish_name = dish[0]
    allergens = set(dish[1]).intersection(SPECIAL_INGREDIENTS)

    return dish_name, allergens

def compile_ingredients(dishes: list[set[str]]) -> set[str]:
    """

    :param dishes: list[set[str]] - List of dish ingredient sets.
    :return: set[str] - .

    This function should return a `set` of all ingredients from all listed dishes.
    """
    all_ingredients = set()

    for dish in dishes:
        all_ingredients.update(dish)
    
    return all_ingredients

def separate_appetizers(dishes, appetizers):
    """

    :param dishes: list[str] - List of dish names.
    :param appetizers: list[str] - List of appetizer names.
    :return: list[str] - List of dish names.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    return set(dishes).difference(set(appetizers))

def singleton_ingredients(dishes: list[set[str]], intersection) -> set[str]:
    """

    :param intersection: constant - One of 
        (VEGAN_INTERSECTION,
        VEGETARIAN_INTERSECTION,
        PALEO_INTERSECTION,
        KETO_INTERSECTION,
        OMNIVORE_INTERSECTION).
    :param dishes: list[set[str]] - List of ingredient sets.
    :return: set[str] - Set of singleton ingredients.

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """
    singletons = set()
    
    for dish in dishes:
        singletons.update(dish.difference(intersection))
        
    return singletons

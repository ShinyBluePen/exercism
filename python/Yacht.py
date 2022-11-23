"""Yacht

https://exercism.org/tracks/python/exercises/yacht
"""

# Heavy thanks to @slahmar for helping with some of the logic.
#  https://exercism.org/tracks/python/exercises/yacht/solutions/slahmar

from random import randrange
from collections import Counter

# Score categories.
# `dice` is a list of 5 ints randomly rolled from 1-6
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES =   lambda dice: count_pips(dice, 1)
TWOS =   lambda dice: count_pips(dice, 2) * 2
THREES = lambda dice: count_pips(dice, 3) * 3
FOURS =  lambda dice: count_pips(dice, 4) * 4
FIVES =  lambda dice: count_pips(dice, 5) * 5
SIXES =  lambda dice: count_pips(dice, 6) * 6
FULL_HOUSE =      lambda dice: sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0
FOUR_OF_A_KIND =  lambda dice: sum(p * 4 for p in set(dice) if dice.count(p) > 3) # credit to CathyQian
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT =    lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum

def score(dice: list[int], category) -> int:
    """Score a "hand" in a game of Yacht.

    https://en.wikipedia.org/wiki/Yacht_(dice_game)
    
    :param dice: - A list of 5 ints ranging in values from 1 to 6.
    :param category: - A prediction of the score, used to score the "hand" for the round.
    :return: - The score of the "hand" for the round.
    """
    return category(dice)

def count_pips(dice, target):
    """Tally the number of occurrences of a pip count from a list of dice.
    
    :param dice: - A list of 5 ints ranging in values from 1 to 6.
    :param target: - The pip count to tally.
    :return: - The number of dice which match the `target` pip count in `dice`.
    """
    return dice.count(target)

def roll() -> list[int]:
    """Roll five 6-sided dice.
    
    :return: - A list of 5 integer values ranging from 1 to 6.
    """
    return [randrange(1, 7) for i in range(1, 6)]

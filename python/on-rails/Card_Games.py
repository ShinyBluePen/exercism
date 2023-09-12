"""Card Games

https://exercism.org/tracks/python/exercises/card-games
"""

import statistics


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: - Current round number.
    :return: - Current round and the two that follow.
    """
    return [number, number+1, number+2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: - First rounds played.
    :param rounds_2: - Second set of rounds played.
    :return: - All rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: - Rounds played.
    :param number: - Round number.
    :return: - True if the round was played.
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: - Cards in hand.
    :return: - Average value of the cards in the hand.
    """
    return statistics.mean(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: - Cards in hand.
    :return: - True if approximate average equals to the `true average`.
    """
    meanlike = card_average(hand)

    return meanlike in ((hand[0] + hand[-1]) / 2, hand[len(hand) // 2])


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: - Cards in hand.
    :return: - Are even and odd averages equal?
    """
    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: - Cards in hand.
    :return: - Hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

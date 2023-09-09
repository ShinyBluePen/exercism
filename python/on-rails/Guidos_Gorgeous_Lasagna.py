"""Guido's Gorgeous Lasagna

https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(minutes: int) -> int:
    """Calculate the bake time remaining.

    :param minutes: - The number of minutes already baked.
    :return: - The number of minutes left until baking is complete.
    """
    
    return EXPECTED_BAKE_TIME - minutes

    
def preparation_time_in_minutes(layers: int) -> int:
    """Calculate necesarry preparation time for the number of `layers`.
    
    :param layers: - The number of layers in the lasagna.
    :return: - The minutes required to prepare n `layers` of lasagna.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total time spent preparing and baking the lasagna.
    
    :param layers: - The number of layers in the lasagna.
    :param elapsed_bake_time: - The minutes elapsed since baking began.
    :return: - The total time spent preparing and baking the lasagna.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time

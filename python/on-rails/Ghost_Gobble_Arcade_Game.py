"""Ghost Gobble Arcade Game

https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game
"""

def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Eat a ghost.

    :param power_pellet_active: Does the player have an active power pellet?
    :param touching_ghost:  Is the player touching a ghost?
    :return: bool
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Increase the player's score.

    :param touching_power_pellet: Does the player have an active power pellet?
    :param touching_dot:  Is the player touching a dot?
    :return: bool
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Lose the game.

    :param power_pellet_active: Does the player have an active power pellet?
    :param touching_ghost: Is the player touching a ghost?
    :return: bool
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Win the game.

    :param has_eaten_all_dots: Has the player "eaten" all the dots?
    :param power_pellet_active: Does the player have an active power pellet?
    :param touching_ghost:  Is the player touching a ghost?
    :return: bool
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
    

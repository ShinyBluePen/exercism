"""Raindrops (Fizzbuzz)

https://exercism.org/tracks/python/exercises/raindrops
"""

def convert(number: int) -> str:
    """Return rain sounds determined by the given `number` if the number matches certain criteria.
    
    :param number: - Generate rain sounds if divisible by 3, 5, or 7.
    :return: - Rain sounds if `number` is divisible by 3, 5, or 7.  Otherwise, return `number` as a string.
    """
    raindrops = []
    if number % 3 == 0: raindrops.append("Pling")
    if number % 5 == 0: raindrops.append("Plang")
    if number % 7 == 0: raindrops.append("Plong")

    return "".join(raindrops) if len(raindrops) else str(number)

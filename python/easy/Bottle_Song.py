"""Bottle Song

https://exercism.org/tracks/python/exercises/bottle-song
"""

NUMBERS = "No One Two Three Four Five Six Seven Eight Nine Ten".split()
    
def recite(start: int=10, take: int=1) -> list[str]:
    """Sing the popular children's song, "Ten Green Bottles".

    There can't be more than 10 bottles on the shelf!  It's not very big.
    
    :param start: - The number of bottles that are initially on the wall.
    :param take: - The number of bottles to take down, one at a time.
    :return: - The collection of verses from each decrement of the `take` from the `start`.
    """
    if start > 10: raise ValueError("Too many bottles on the shelf!")
    
    out = []
    for i in range(start, start - take, -1):
        out.append(f"{bottles(i)} hanging on the wall,")
        out.append(f"{bottles(i)} hanging on the wall,")
        out.append("And if one green bottle should accidentally fall,")
        out.append(f"There'll be {bottles(i - 1).lower()} hanging on the wall.")
        out.append("")
        
    return out[:-1]

def bottles(num: int) -> str:
    """Return the bottle term."""
    out = f"{NUMBERS[num]} green bottle"
    if num != 1:
        out += "s"
    return out

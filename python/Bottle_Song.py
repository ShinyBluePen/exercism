"""Bottle Song

https://exercism.org/tracks/python/exercises/bottle-song
"""

_num_words = "no one two three four five six seven eight nine ten".split()
NUM_TO_WORD = {num: word for word, num in zip(_num_words, range(len(_num_words)))}
    
def recite(start: int=10, take: int=1) -> list[str]:
    """Sing the popular children's song, "Ten Green Bottles".

    There can't be more than 10 bottles on the shelf!  It's not very big.
    
    :param start: - The number of bottles that are initially on the wall.
    :param take: - The number of bottles to take down, one at a time.
    :return: - The collection of verses from each decrement of the `take` from the `start`.
    """
    if start > 10: raise ValueError("Too many bottles on the shelf!")
    song = []
    for bottles in range(start, 0, -1):
        take -= 1
        song += [
            f"{NUM_TO_WORD[bottles].title()} green bottle{'' if bottles == 1 else 's'} hanging on the wall,",
            f"{NUM_TO_WORD[bottles].title()} green bottle{'' if bottles == 1 else 's'} hanging on the wall,",
            f"And if one green bottle should accidentally fall,",
            f"There'll be {NUM_TO_WORD[bottles-1]} green bottle{'' if bottles-1 == 1 else 's'} hanging on the wall."
        ]
        
        if take: 
            song.append("")
        else: 
            break

    return song

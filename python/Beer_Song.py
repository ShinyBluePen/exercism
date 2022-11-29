"""Beer Song

https://exercism.org/tracks/python/exercises/beer-song

@tomdml had a really concise solution to this.
https://exercism.org/tracks/python/exercises/beer-song/solutions/tomdml
"""

def recite(start: int=10, take: int=1) -> list[str]:
    """Sing the popular "Bottles of beer on the wall" song.
    
    :param start: - The initial number of bottles on the wall.
    :param take: - The number of bottles to take down from the wall.
    :return: - A list of each line of the song, "99 bottles of beer" 
               from `start` until `take` is exhausted.
    """
    b_count = start
    song = []
    while take:
        # it's a lot more readable to just handle conditions b_count is 0, 1, 2
        #   but it's more lines.  Idk.  I think it's probably better to err on 
        #   the side of readability as being more important
        if b_count is 0:
            song.append("No more bottles of beer on the wall, no more bottles of beer.")
            song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
            take -= 1    # this isn't needed for the exercise,
            b_count = 99 #   but it should wrap.  It's how it should be
            continue
        if b_count is 1:
            song.append("1 bottle of beer on the wall, 1 bottle of beer.")
            song.append("Take it down and pass it around, no more bottles of beer on the wall.")
            if take > 1: song.append("")
            take -= 1
            b_count -= 1
            continue
        if b_count is 2:
            song.append("2 bottles of beer on the wall, 2 bottles of beer.")
            song.append("Take one down and pass it around, 1 bottle of beer on the wall.")
            if take > 1: song.append("")
            take -= 1
            b_count -= 1
            continue

        song.append(f"{b_count} bottles of beer on the wall, {b_count} bottles of beer.")
        song.append(f"Take one down and pass it around, {b_count-1} bottles of beer on the wall.")
        if take > 1: song.append("")
        take -= 1
        b_count -= 1

    return song

"""House

https://exercism.org/tracks/python/exercises/house
"""

def recite(start_verse: int=12, end_verse: int=12) -> list[str]:
    """Recite the nursery rhyme 'This is the House that Jack Built'.

    Recite the entire song from the given starting verse, continuing
    to recite the entire song while moving through the range of
    start_verse to end_verse...  Why would you do this...?
    
    :param start_verse: - Start reciting the song from this verse.
    :param end_verse: - Stop reciting the song from this verse.
    :return: - List of song recitations from `start_verse` to `end_verse`.
    """
    VERSE_LINES = [
        'the house that Jack built.',
        'the malt that lay in',
        'the rat that ate',
        'the cat that killed',
        'the dog that worried',
        'the cow with the crumpled horn that tossed',
        'the maiden all forlorn that milked',
        'the man all tattered and torn that kissed',
        'the priest all shaven and shorn that married',
        'the rooster that crowed in the morn that woke',
        'the farmer sowing his corn that kept',
        'the horse and the hound and the horn that belonged to']
    
    return [f"This is {' '.join(VERSE_LINES[i-1::-1])}" for i in range(start_verse, end_verse+1)]

    # ## Take 1; it's a lot messier
    # # I put things in the lists in the wrong order and I can't be bothered to re-do them
    # NOUN = ["horse and the hound and the horn",
    #         "farmer sowing his corn",
    #         "rooster that crowed in the morn",
    #         "priest all shaven and shorn",
    #         "man all tattered and torn",
    #         "maiden all forlorn",
    #         "cow with the crumpled horn",
    #         "dog",
    #         "cat",
    #         "rat",
    #         "malt",
    #         "house that Jack built.",]
    # NOUN.reverse()
    # VERB = ["belonged to",
    #         "kept",
    #         "woke",
    #         "married",
    #         "kissed",
    #         "milked",
    #         "tossed",
    #         "worried",
    #         "killed",
    #         "ate",
    #         "lay in",]
    # VERB.reverse()

    # song = []
    # lyrics = []
    # while start_verse <= end_verse:
    #     # we need to -1 start_verse in the range because this exercise indexes by 1
    #     for i in range(start_verse-1, -1, -1):
    #         if i == start_verse - 1:
    #             lyrics.append(f"This is the {NOUN[i]}")
    #         else:
    #             lyrics.append(f"that {VERB[i]} the {NOUN[i]}")

    #     song.append(" ".join(lyrics))
    #     lyrics = []
    #     start_verse += 1

    # return song

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

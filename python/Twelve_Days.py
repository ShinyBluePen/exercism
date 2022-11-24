"""Twelve Days

https://exercism.org/tracks/python/exercises/twelve-days
"""

def recite(start_verse: int=12, end_verse: int=12) -> str:
    """Return the 12 Days of Christmas.  May specify optional start and end verses.
    
    :param start_verse: - Start reciting the carol from this verse.
    :param end_verse: - Stop reciting the carol from this verse.
    :return carol: - Recite the carol from the `start_verse` to the `end_verse`.
    """
    ordinal = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
    ]
    gift = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
    ]
    
    carol = []
    for verse in range(start_verse, end_verse+1):
        carol.append(f"On the {ordinal[verse-1]} day of Christmas my true love gave to me: "
                     f"{', '.join(gift[verse-1:0:-1])}"
                     f"{', and ' if verse > 1 else ''}"
                     f"{gift[0]}.")
    
    return carol

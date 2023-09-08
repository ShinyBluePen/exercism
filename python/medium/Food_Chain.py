"""Food Chain

https://exercism.org/tracks/python/exercises/food-chain
"""

_ = "that wriggled and jiggled and tickled inside her."
AMC = [ # ANIMALS_MOTIVES_COMMENTS
    ["fly",     None,                                              None],
    ["spider",  "She swallowed the spider to catch the fly.",      "It wriggled and jiggled and tickled inside her."],
    ["bird",   f"She swallowed the bird to catch the spider {_}",  "How absurd to swallow a bird!"],
    ["cat",     "She swallowed the cat to catch the bird.",        "Imagine that, to swallow a cat!"],
    ["dog",     "She swallowed the dog to catch the cat.",         "What a hog, to swallow a dog!"],
    ["goat",    "She swallowed the goat to catch the dog.",        "Just opened her throat and swallowed a goat!"],
    ["cow",     "She swallowed the cow to catch the goat.",        "I don't know how she swallowed a cow!"],
    ["horse",   None,                                              "She's dead, of course!"],
]

def recite(start: int=1, stop:int=8) -> list[str]:
    """Sing "I know an old lady who swallowed a fly".
    
    :param start: - The verse from which to start the song.
    :param stop: - The final verse of the song to sing.
    :return: - The slice of the song specified by `start` and `stop`.
    """
    song = []
    start -= 1
    while start < stop:
        animal, motive, comment = AMC[start]
        song.append(f"I know an old lady who swallowed a {animal}.")
        song.append(f"{comment}") if comment else None
        
        if animal == "horse": break
            
        song += [AMC[verse][1] for verse in range(start, 0, -1) if AMC[verse][1]]
        
        song.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        start += 1
        
        if start < stop: song.append("")
            
    return song

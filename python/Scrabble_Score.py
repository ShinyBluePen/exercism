"""Scrabble Score

https://exercism.org/tracks/python/exercises/scrabble-score

https://en.wikipedia.org/wiki/Scrabble
"""

class Tile:
    """Representation of a Scrabble word letter tile object.
    
    Attributes:
    :SCORE_DATA: dict{int: str} - Constant for the score values of each letter.
    :letter: str - The letter of the `Tile`.
    :score: int - The score of the `Tile`.
    """
    SCORE_DATA = {
        1: "AEIOULNRST",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ",
    }
    def __init__(self, letter: str) -> object:
        self.letter = letter.upper()
        self.score = 0
        
        for score, letters in Tile.SCORE_DATA.items():
            if self.letter in letters:
                self.score = score
                
    def __add__(self, other):
        return self.score + other

    def __radd__(self, other):
        return other + self.score

    def __str__(self):
        return self.letter
    
def score(word: str) -> int:
    """Calculate the score of a word in Scrabble.
    
    :param word: - A string forming a - hopefully - valid word, like "AA".
    :return: - The summed score of each individual `Tile` in the word.
    """
    return sum([Tile(letter) for letter in word])
    

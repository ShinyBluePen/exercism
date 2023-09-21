"""Hangman

https://exercism.org/tracks/python/exercises/hangman
"""

STATUS_WIN = 1
STATUS_LOSE = -1
STATUS_ONGOING = 0

import string

class Hangman:
    """Hangman is a word guessing game where the player attempts to guess a 
    hidden word, letter by letter, within a limited number of guesses.

    Parameters:
    ----------
    word: str - The secret word that the player is trying to guess.

    Attributes:
    ----------
    word: str - The secret word.
    mask: list[str] - A list representing the current state of guessed and hidden 
                      letters in the word, with '_' for hidden letters.
    remaining_guesses: int - The number of remaining incorrect guesses allowed.
    status: str - The current status of the game, which can be 'win', 'lose', or 'ongoing'.

    Methods:
    --------
    guess(char: str) -> None:
        Make a guess for a character in the word. Updates the game state based on the guess.

    get_masked_word() -> str:
        Return the word with guessed letters revealed and hidden letters masked as '_'.

    get_status() -> str:
        Return the current status of the game, which can be 'win', 'lose', or 'ongoing'.
    """
    def __init__(self, word: str):
        self.word = word
        self.guesses = set()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char: str) -> None:
        """Guess a letter that could be in the word."""
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        if char not in string.ascii_lowercase:
            raise ValueError(f"Expected an alphabetical character, got: {char}")
        
        if char in self.guesses or char not in self.word:
            self.remaining_guesses -= 1
            
        self.guesses.add(char)

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

        if set(self.word).issubset(self.guesses):
            self.status = STATUS_WIN
            
    def get_masked_word(self) -> str:
        """Return the letters of the word revealed so far."""
        return "".join(c if c in self.guesses else "_" for c in self.word)

    def get_status(self) -> str:
        """Return the status of the game."""
        return self.status

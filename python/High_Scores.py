"""High Scores

https://exercism.org/tracks/python/exercises/high-scores
"""

class HighScores:
    """Keep track of a players' high scores in a game.
    
    Parameters:
    :param scores: list[int] - The players initial high scores.
    
    Attributes:
    :scores: list[int] - The players current high scores.
    
    Methods:
    :latest(self): - The players most recent score.
    :personal_best(self): - The players highest all-time score.
    :personal_top_three(self): - The players 3 highest all-time scores.
    
    Raises:
    None
    """
    def __init__(self, scores: int):
        self.scores = scores

    def latest(self) -> list[int]:
        return self.scores[-1]
    
    def personal_best(self) -> int:
        return max(self.scores)
    
    def personal_top_three(self) -> list[int]:
        return sorted(self.scores, reverse=True)[:3]

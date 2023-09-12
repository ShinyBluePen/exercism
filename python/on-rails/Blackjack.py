"""Black Jack

https://exercism.org/tracks/python/exercises/black-jack

How to play blackjack:
    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards:
    https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

CARD_VALUES = {
    "A": 1,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1,
}


def value_of_card(card: str) -> str:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical 
                   value otherwise.
    """
    return CARD_VALUES[card]


def higher_card(card_one: str, card_two: str) -> str:
    """Determine which card has a higher value in the hand.

    :param card_one: - A dealt card.
    :param card_two: - Another dealt card.
    :return: - The card with the highest value or a tuple of both cards 
               if they are of equal value.
    """
    c1, c2 = value_of_card(card_one), value_of_card(card_two)
    
    return (card_one, card_two) if c1 == c2 else card_one if c1 > c2 else card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one: - A dealt card.
    :param card_two: - Another dealt card.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    c1, c2 = value_of_card(card_one), value_of_card(card_two)

    return 1 if c1 + c2 + 11 > 21 else 1 if card_one == "A" or card_two == "A" else 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a natural blackjack.

    :param card_one: - A dealt card.
    :param card_two: - Another dealt card.
    :return: - True if the hand is a blackjack (two cards worth 21).
    """
    tens = "J Q K 10".split()
    return (
        card_one == "A" and card_two in tens or 
        card_two == "A" and card_one in tens
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one: - A dealt card.
    :param card_two: - Another dealt card.
    :return: - True if the hand can be split into two pairs (i.e. cards 
               are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one: - A dealt card.
    :param card_two: - Another dealt card.
    :return: - True if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    hand_sum = value_of_card(card_one) + value_of_card(card_two)

    return hand_sum in [9, 10, 11]

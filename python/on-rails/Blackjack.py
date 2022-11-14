"""Blackjack

Functions to help play and score a game of blackjack.
 
https://exercism.org/tracks/python/exercises/black-jack
How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
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

def value_of_card(card):
    """Determine the scoring value of a card.
 
    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    card = card.upper()
    
    if card in CARD_VALUES:
        card = CARD_VALUES.get(card)
        return card
    else:
        print("Please enter a valid card!")
        
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
 
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    high_card = None
    card_one = card_one.upper()
    card_two = card_two.upper()
    
    if card_one in CARD_VALUES and card_two in CARD_VALUES:
        c1v = value_of_card(card_one)
        c2v = value_of_card(card_two)
    
        if c1v > c2v:
            high_card = card_one
        elif c2v > c1v:
            high_card = card_two
        else:
            high_card = (card_one, card_two)
    else:
        print("please enter valid cards!")
    
    return high_card
  
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
 
    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.
 
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    ace = 11
    card_one = card_one.upper()
    card_two = card_two.upper()
    
    c1v = value_of_card(card_one)
    c2v = value_of_card(card_two)
    
    if card_one == "A" or card_two == "A":
        ace = 1
    if c1v + c2v + ace > 21:
        ace = 1
        
    return ace
  
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
 
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    blackjack = False
    
    # dirty hack the value of aces for this function.
    CARD_VALUES["A"] = 11
    
    card_one = card_one.upper()
    card_two = card_two.upper()
    c1v = value_of_card(card_one)
    c2v = value_of_card(card_two)
    
    if c1v + c2v == 21:
        blackjack = True
        
    CARD_VALUES["A"] = 1
    
    return blackjack
  
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
 
    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    can_split = False
    card_one = card_one.upper()
    card_two = card_two.upper()
    c1v = value_of_card(card_one)
    c2v = value_of_card(card_two)
    
    if c1v == c2v:
        can_split = True
        
    return can_split
  
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
 
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    can_double = False
    card_one = card_one.upper()
    card_two = card_two.upper()
    c1v = value_of_card(card_one)
    c2v = value_of_card(card_two)
    
    if c1v + c2v == 9 or c1v + c2v == 10 or c1v + c2v == 11:
        can_double = True
        
    return can_double

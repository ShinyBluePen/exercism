"""Poker

https://exercism.org/tracks/python/exercises/poker
"""

import collections

def best_hands(hands: list[str]) -> list[str]:
    """Determine a winning hand in texas hold'em poker.

    https://en.wikipedia.org/wiki/Texas_hold_%27em
    
    :param hands: - A list of hands represented as strings, ex: ["4D 5S 6S 8D 3C"].
    :return: - A list with the winning hand(s if any ties).
    """
    _hand_ranking = ("straight flush.four of a kind.full house.flush.straight.three of a kind.two pair.two of a kind.high card").split(".")
    _cards = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    
    HAND_RANKING = {rank: value for rank, value in zip(_hand_ranking, range(9, 0, -1))}
    CARDS = {card: value for card, value in zip(_cards, range(2, 15))}
    
    def evaluate(hands: list[str]) -> list[str]:
        """Score each hand and return any winning hands."""
        hand_data = []
        for hand in hands:
            h = parse(hand)
            for f in rank():
                h = f(h)
                if h["score"]: # only hits if an is_{hand} hits
                    hand_data.append(h)
                    break # highest hand rank for this hand hit

        # break tie hand scores with hand kickers and handle potential hand ties
        hand_data.sort(key=lambda x: x["score"], reverse=True)
        top_score = hand_data[0]["score"]
        top_hand = hand_data[0]["hand"]
        top_kicker = hand_data[0]["kicker"]

        for h in hand_data:
            if h["score"] == top_score:
                if h["kicker"] > top_kicker:
                    top_kicker = h["kicker"]
                    top_hand = h["hand"]

        # determine round winning hands
        return [h["hand"] for h in hand_data if h["kicker"] == top_kicker]
    
    def parse(hand: str) -> dict:
        """Extract useful information out of the raw hand.
        
        Return a dictionary of that information with the values:
        "score": int, 
        "pairs": list[int], 
        "values": list[int], 
        "kicker": list[int], 
        "hand": str
        """
        # `i[:-1]` cuts off the suit from the card
        values = sorted([CARDS[i[:-1]] for i in hand.split()])
        
        ## kicker must be sorted this way to properly grade two pair hands
        # sort the values from highest to lowest
        kicker = sorted(set(values), reverse=True)
        # sort the values based on how many occur, from most to least
        kicker = sorted(kicker, key=values.count, reverse=True)
        
        pairs = sorted([values.count(i) for i in set(values)], reverse=True)
        
        score = 0

        h = {"score": score, "pairs": pairs, "values": values, "kicker": kicker, "hand": hand}
        
        return h
    
    def rank() -> list:
        """Return a list of single-hand ranking functions
        
        https://en.wikipedia.org/wiki/List_of_poker_hands.
        """
        return [is_straight_flush,
                is_four_kind, 
                is_full_house,
                is_flush,
                is_straight,
                is_three_kind, 
                is_two_pair,
                is_two_kind, 
                is_high_card,]
    
    def is_straight_flush(hand: dict) -> dict:
        """Check if hand is a straight flush."""
        if (is_straight(hand)["score"] == HAND_RANKING["straight"] and 
            is_flush(hand)["score"]    == HAND_RANKING["flush"]):
            hand["score"] = HAND_RANKING["straight flush"]
                 
        return hand

    def is_four_kind(hand: dict) -> dict:
        """Check if hand is a four of a kind."""
        if hand["pairs"] == [4, 1]:
            hand["score"] = HAND_RANKING["four of a kind"]
    
        return hand

    def is_full_house(hand: dict) -> dict:
        """Check if hand is a full house."""
        if hand["pairs"] == [3, 2]:
            hand["score"] = HAND_RANKING["full house"]
    
        return hand

    def is_flush(hand: dict) -> dict:
        """Check if hand is a flush."""
        # [i[-1] is the last element, or the suit, of each card
        if len(set([i[-1] for i in hand["hand"].split()])) == 1:
            hand["score"] = HAND_RANKING["flush"]

        return hand

    def is_straight(hand: dict) -> dict:
        """Check if hand is a straight."""
        # 5 high straight
        _ = CARDS
        if hand["values"] == ([_["2"], _["3"], _["4"], _["5"], _["A"]]):
            hand["values"][-1] = 1
            hand["kicker"][0] = 1
            hand["score"] = HAND_RANKING["straight"]

        if hand["values"] == list(range(min(hand["values"]), max(hand["values"])+1)):
            hand["score"] = HAND_RANKING["straight"]

        return hand

    def is_three_kind(hand: dict) -> dict:
        """Check if hand is a three of a kind."""
        if hand["pairs"] == [3, 1, 1]:
            hand["score"] = HAND_RANKING["three of a kind"]
    
        return hand

    def is_two_pair(hand: dict) -> dict:
        """Check if hand is a two pair."""
        if hand["pairs"] == [2, 2, 1]:
            hand["score"] = HAND_RANKING["two pair"]
    
        return hand

    def is_two_kind(hand: dict) -> dict:
        """Check if hand is a two of a kind."""
        if hand["pairs"] == [2, 1, 1, 1]:
            hand["score"] = HAND_RANKING["two of a kind"]
    
        return hand

    def is_high_card(hand: dict) -> dict:
        """Check if hand is high card."""
        if hand["pairs"] == [1, 1, 1, 1, 1]:
            hand["score"] = HAND_RANKING["high card"]
        
        return hand
    
    return evaluate(hands)

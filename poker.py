from collections import Counter
from card import Card

CATEGORY_RANKS = {'High Card': 0, 'One Pair': 1}

def get_high_card(cards):
    """ Évalue une high card """
    sorted_cards = sorted(cards, reverse=True) 
    chosen = sorted_cards[:5]
    ranks = tuple(c.rank for c in chosen)
    return 'High Card', chosen, (0,) + ranks

def evaluate_hand(cards):
    if len(cards) != 7:
        raise ValueError("Une main doit avoir exactement 7 cartes")
    return get_high_card(cards)
from collections import Counter
from card import Card

CATEGORY_RANKS = {'High Card': 0, 'One Pair': 1, 'Two Pair': 2, 'Three of a Kind': 3}

def get_high_card(cards):
    """ Évalue une high card """
    sorted_cards = sorted(cards, reverse=True) 
    chosen = sorted_cards[:5]
    ranks = tuple(c.rank for c in chosen)
    return 'High Card', chosen, (0,) + ranks

def get_one_pair(cards):
    """Détecte une paire"""
    rank_count = Counter(c.rank for c in cards)
    pairs = sorted([r for r, count in rank_count.items() if count >= 2], reverse=True)
    if not pairs:
        return None
    
    pair_rank = pairs[0]
    pair_cards = sorted([c for c in cards if c.rank == pair_rank], reverse=True)[:2]
    kickers = sorted([c for c in cards if c.rank != pair_rank], reverse=True)[:3]
    chosen = pair_cards + kickers
    key = (pair_rank,) + tuple(c.rank for c in kickers)
    return 'One Pair', chosen, (1,) + key

def get_two_pair(cards):
    """Détecte deux paires"""
    rank_count = Counter(c.rank for c in cards)
    pairs = sorted([r for r, count in rank_count.items() if count >= 2], reverse=True)
    if len(pairs) < 2:
        return None
    
    high_pair_rank = pairs[0]
    low_pair_rank = pairs[1]
    
    high_pair_cards = sorted([c for c in cards if c.rank == high_pair_rank], reverse=True)[:2]
    low_pair_cards = sorted([c for c in cards if c.rank == low_pair_rank], reverse=True)[:2]
    kicker = sorted([c for c in cards if c.rank not in (high_pair_rank, low_pair_rank)], reverse=True)[:1]
    
    chosen = high_pair_cards + low_pair_cards + kicker
    key = (high_pair_rank, low_pair_rank) + tuple(c.rank for c in kicker)
    return 'Two Pair', chosen, (2,) + key

def get_three_kind(cards):
    """Détecte un brelan"""
    rank_count = Counter(c.rank for c in cards)
    threes = sorted([r for r, count in rank_count.items() if count >= 3], reverse=True)
    if not threes:
        return None
    
    three_rank = threes[0]
    three_cards = sorted([c for c in cards if c.rank == three_rank], reverse=True)[:3]
    kickers = sorted([c for c in cards if c.rank != three_rank], reverse=True)[:2]
    
    chosen = three_cards + kickers
    key = (three_rank,) + tuple(c.rank for c in kickers)
    return 'Three of a Kind', chosen, (3,) + key

def evaluate_hand(cards):
    tk = get_three_kind(cards)
    if tk:
        return tk
    
    tp = get_two_pair(cards)
    if tp:
        return tp
    
    op = get_one_pair(cards)
    if op:
        return op
    
    return get_high_card(cards)
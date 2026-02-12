from collections import Counter
from card import Card

CATEGORY_RANKS = {'High Card': 0, 'One Pair': 1, 'Two Pair': 2, 'Three of a Kind': 3, 'Straight': 4, 'Flush': 5, 'Full House': 6, 'Four of a Kind': 7, 'Straight Flush': 8}

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

def get_straight(cards):
    """Détecte une straight, wheel"""
    ranks_set = set(c.rank for c in cards)
    
    if {14, 2, 3, 4, 5}.issubset(ranks_set):
        straight_ranks = [5, 4, 3, 2, 14]
        chosen = []
        for r in straight_ranks:
            card = next(c for c in cards if c.rank == r)
            chosen.append(card)
        key = (5, 4, 3, 2, 1)  
        return 'Straight', chosen, (4,) + key
    
    sorted_ranks = sorted(ranks_set)
    for i in range(len(sorted_ranks) - 4):
        if sorted_ranks[i + 4] - sorted_ranks[i] == 4:
            straight_ranks = sorted_ranks[i:i + 5][::-1]
            chosen = []
            for r in straight_ranks:
                card = next(c for c in cards if c.rank == r)
                chosen.append(card)
            key = tuple(straight_ranks)
            return 'Straight', chosen, (4,) + key
    return None
def get_flush(cards):
    """Détecte une flush"""
    suit_count = Counter(c.suit for c in cards)
    flush_suits = [s for s, count in suit_count.items() if count >= 5]
    if not flush_suits:
        return None
    
    suit = flush_suits[0]
    flush_cards = sorted([c for c in cards if c.suit == suit], reverse=True)
    chosen = flush_cards[:5]
    ranks = [c.rank for c in chosen]
    key = tuple(ranks)
    return 'Flush', chosen, (5,) + key

def get_full_house(cards):
    """Détecte un full house"""
    rank_count = Counter(c.rank for c in cards)
    threes = sorted([r for r, count in rank_count.items() if count >= 3], reverse=True)
    pairs = sorted([r for r, count in rank_count.items() if count >= 2], reverse=True)
    if not threes or len(pairs) < 2:
        return None
    
    three_rank = threes[0]
    pair_rank = next(p for p in pairs if p != three_rank)
    
    three_cards = sorted([c for c in cards if c.rank == three_rank], reverse=True)[:3]
    pair_cards = sorted([c for c in cards if c.rank == pair_rank], reverse=True)[:2]
    
    chosen = three_cards + pair_cards
    key = (three_rank, pair_rank)
    return 'Full House', chosen, (6,) + key

def get_four_kind(cards):
    """Détecte un carré"""
    rank_count = Counter(c.rank for c in cards)
    fours = [r for r, count in rank_count.items() if count >= 4]
    if not fours:
        return None
    
    four_rank = fours[0]
    four_cards = sorted([c for c in cards if c.rank == four_rank], reverse=True)[:4]
    kicker = sorted([c for c in cards if c.rank != four_rank], reverse=True)[:1]
    
    chosen = four_cards + kicker
    key = (four_rank, kicker[0].rank)
    return 'Four of a Kind', chosen, (7,) + key

def get_straight_flush(cards):
    """Détecte une straight flush"""
    suit_count = Counter(c.suit for c in cards)
    flush_suits = [s for s, count in suit_count.items() if count >= 5]
    for suit in flush_suits:
        suit_cards = [c for c in cards if c.suit == suit]
        st = get_straight(suit_cards)
        if st:
            return 'Straight Flush', st[1], (8,) + st[2][1:]  # st[2] = (4,) + key, on prend key
    return None

def evaluate_hand(cards):

    sf = get_straight_flush(cards)
    if sf:
        return sf

    fk = get_four_kind(cards)
    if fk:
        return fk
    
    fh = get_full_house(cards)
    if fh:
        return fh

    fl = get_flush(cards)
    if fl:
        return fl

    st = get_straight(cards)
    if st:
        return st
    
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
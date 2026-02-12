from card import Card
from poker import evaluate_hand

def test_card_creation():
    card = Card('A', 'H')
    assert card.rank == 14 
    assert card.suit == 'H'

def test_card_equality():
    """Test que deux cartes identiques sont égales"""
    card1 = Card('A', 'H')
    card2 = Card('A', 'H')
    card3 = Card('K', 'H')
    assert card1 == card2
    assert card1 != card3

def test_card_repr():
    """Test de l'affichage d'une carte"""
    card = Card('A', 'H')
    assert repr(card) == 'AH'
    card2 = Card('10', 'S')
    assert repr(card2) == '10S'

def test_card_comparison():
    """Test de la comparaison entre cartes"""
    high_card = Card('A', 'H')
    low_card = Card('K', 'H')
    same_rank_diff_suit = Card('A', 'D')

    assert high_card > low_card
    assert high_card != same_rank_diff_suit

def test_high_card():
    """Test détection high card"""
    cards = [Card('A','H'), Card('K','D'), Card('Q','C'), Card('J','S'), Card('9','H'), Card('8','D'), Card('7','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'High Card'
    assert len(chosen) == 5
    assert set(chosen).issubset(set(cards))
    ranks = [c.rank for c in chosen]
    assert ranks == [14, 13, 12, 11, 9]  

def test_one_pair():
    cards = [Card('A','H'), Card('A','D'), Card('K','C'), Card('Q','S'), Card('J','H'), Card('9','D'), Card('8','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'One Pair'
    assert len(chosen) == 5
    ranks = sorted([c.rank for c in chosen])
    assert ranks.count(14) == 2 
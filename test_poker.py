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

def test_two_pair():
    cards = [Card('A','H'), Card('A','D'), Card('K','C'), Card('K','S'), Card('J','H'), Card('9','D'), Card('8','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Two Pair'
    ranks = sorted([c.rank for c in chosen])
    assert ranks.count(14) == 2 and ranks.count(13) == 2  # Paire d'As et de Rois

def test_three_kind():
    cards = [Card('A','H'), Card('A','D'), Card('A','C'), Card('K','S'), Card('J','H'), Card('9','D'), Card('8','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Three of a Kind'
    ranks = sorted([c.rank for c in chosen])
    assert ranks.count(14) == 3 

def test_straight():
    cards = [Card('9','H'), Card('8','D'), Card('7','C'), Card('6','S'), Card('5','H'), Card('K','D'), Card('Q','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Straight'
    ranks = sorted([c.rank for c in chosen])
    assert ranks == [5,6,7,8,9]

def test_wheel_straight():
    cards = [Card('A','H'), Card('2','D'), Card('3','C'), Card('4','S'), Card('5','H'), Card('K','D'), Card('Q','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Straight'
    ranks = sorted([c.rank for c in chosen])
    assert ranks == [2,3,4,5,14] 

def test_flush():
    cards = [Card('A','H'), Card('J','H'), Card('9','H'), Card('4','H'), Card('2','C'), Card('6','H'), Card('K','D')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Flush'
    suits = [c.suit for c in chosen]
    assert all(s == 'H' for s in suits) 
    ranks = sorted([c.rank for c in chosen], reverse=True)
    assert ranks == [14,11,9,6,4]  

def test_full_house():
    cards = [Card('A','H'), Card('A','D'), Card('A','C'), Card('K','S'), Card('K','H'), Card('9','D'), Card('8','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Full House'
    ranks = sorted([c.rank for c in chosen])
    assert ranks.count(14) == 3 and ranks.count(13) == 2  # Trois As, deux Rois

def test_four_kind():
    cards = [Card('A','H'), Card('A','D'), Card('A','C'), Card('A','S'), Card('K','H'), Card('9','D'), Card('8','C')]
    cat, chosen, key = evaluate_hand(cards)
    assert cat == 'Four of a Kind'
    ranks = sorted([c.rank for c in chosen])
    assert ranks.count(14) == 4
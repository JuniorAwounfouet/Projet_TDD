from card import Card

def test_card_creation():
    card = Card('A', 'H')
    assert card.rank == 14  # A = 14
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

    assert high_card > low_card  # A > K
    assert high_card == same_rank_diff_suit  # Même rang, ordre des couleurs
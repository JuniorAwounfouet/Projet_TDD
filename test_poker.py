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
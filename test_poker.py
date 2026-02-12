from card import Card

def test_card_creation():
    card = Card('A', 'H')
    assert card.rank == 14  # A = 14
    assert card.suit == 'H'
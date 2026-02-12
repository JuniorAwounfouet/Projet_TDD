from collections import Counter
from card import Card

CATEGORY_RANKS = {'High Card': 0}

def get_high_card(cards):
    """
    Évalue une high card
    Retourne: (catégorie, 5_cartes_choisies, clé_de_tri)
    """
    sorted_cards = sorted(cards, reverse=True)  # Trie décroissant
    chosen = sorted_cards[:5]  # Les 5 meilleures
    ranks = tuple(c.rank for c in chosen)
    return 'High Card', chosen, (0,) + ranks

def evaluate_hand(cards):
    """Fonction principale d'évaluation"""
    if len(cards) != 7:
        raise ValueError("Une main doit avoir exactement 7 cartes")
    return get_high_card(cards)
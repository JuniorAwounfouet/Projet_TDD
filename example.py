from card import Card
from poker import evaluate_hand, find_winners

def main():
    print("=== Exemple 1: Évaluation d'une main ===")
    cards = [
        Card('A', 'H'), Card('K', 'D'), Card('Q', 'C'), Card('J', 'S'),
        Card('10', 'H'), Card('9', 'D'), Card('8', 'C')
    ]
    category, chosen, key = evaluate_hand(cards)
    print(f"Cartes: {[str(c) for c in cards]}")
    print(f"Catégorie: {category}")
    print(f"5 cartes choisies: {[str(c) for c in chosen]}")
    print()

    print("=== Exemple 2: Comparaison de joueurs ===")
    board = [Card('A', 'H'), Card('K', 'D'), Card('Q', 'C'), Card('J', 'S'), Card('9', 'H')]
    players = [
        [Card('10', 'D'), Card('8', 'C')],  
        [Card('10', 'S'), Card('7', 'C')]   
    ]

    winners, results = find_winners(board, players)
    print(f"Board: {[str(c) for c in board]}")
    for i, (cat, chosen, key) in enumerate(results):
        print(f"Joueur {i+1}: {cat} - {[str(c) for c in chosen]}")
    print(f"Gagnants: Joueur(s) {[i+1 for i in winners]}")
    print()

    print("=== Exemple 3: Royal Flush ===")
    royal_cards = [
        Card('A', 'H'), Card('K', 'H'), Card('Q', 'H'), Card('J', 'H'),
        Card('10', 'H'), Card('9', 'D'), Card('8', 'C')
    ]
    category, chosen, key = evaluate_hand(royal_cards)
    print(f"Cartes: {[str(c) for c in royal_cards]}")
    print(f"Catégorie: {category}")
    print(f"5 cartes choisies: {[str(c) for c in chosen]}")

if __name__ == "__main__":
    main()
class Card:
    RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    SUITS = {'H': 0, 'D': 1, 'C': 2, 'S': 3}

    def __init__(self, rank_str, suit):
        self.rank = self.RANKS[rank_str]
        self.suit = suit

    def __eq__(self, other):
        """Deux cartes , même couleur"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))
    
    def __repr__(self):
        rank_str = {v: k for k, v in self.RANKS.items()}[self.rank]
        return f"{rank_str}{self.suit}"

    def __lt__(self, other):
        """Comparaison:rang,couleur"""
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.SUITS[self.suit] < self.SUITS[other.suit]
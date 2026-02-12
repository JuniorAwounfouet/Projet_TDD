# Texas Hold'em Poker Hand Evaluator

This project implements a Texas Hold'em poker hand evaluator and comparer using TDD.

## Features

- Evaluates poker hands from 7 cards (5 board + 2 hole)
- Determines the best 5-card hand
- Compares multiple players and finds winners (including ties)
- Supports all standard poker hand categories

## Hand Categories (highest to lowest)

1. Straight Flush
2. Four of a Kind
3. Full House
4. Flush
5. Straight
6. Three of a Kind
7. Two Pair
8. One Pair
9. High Card

## Chosen 5 Cards Ordering

The chosen5 cards are ordered consistently for deterministic output:

- **Straight / Straight Flush**: In straight order, highest to lowest (e.g., A K Q J 10 for ace-high, 5 4 3 2 A for wheel)
- **Flush**: Descending ranks
- **Four of a Kind**: Four matching cards first (by rank), then kicker
- **Full House**: Three of a kind first, then pair
- **Three of a Kind**: Three matching cards first, then kickers descending
- **Two Pair**: Higher pair, lower pair, kicker
- **One Pair**: Pair first, then kickers descending
- **High Card**: Descending ranks

## Assumptions

- No duplicate cards in input
- Valid input: exactly 7 distinct cards per hand

## Usage

```python
from card import Card
from poker import evaluate_hand, find_winners

# Evaluate single hand
cards = [Card('A','H'), Card('K','H'), ...]  # 7 cards
category, chosen5, key = evaluate_hand(cards)

# Compare players
board = [Card('A','H'), ...]  # 5 cards
players = [[Card('K','D'), Card('Q','C')], ...]  # list of [hole1, hole2]
winners, results = find_winners(board, players)
# winners: list of player indices that win
# results: list of (category, chosen5, key) for each player
```

## Testing

Run tests with pytest:

```bash
pytest
```
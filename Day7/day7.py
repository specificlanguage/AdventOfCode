from collections import Counter
from heapq import heappush
FILENAME = "d7input"

CARD_ORDER = "J23456789TQKA"

def scoreHand(hand):
    first_joker = hand.find('J')
    if first_joker > -1:
        return max([scoreHand(hand[:first_joker] + joker_value + hand[first_joker + 1:]) for joker_value in CARD_ORDER[1:]])
    counter = Counter(hand)
    n = len(counter)
    if n == 1:
        return 6
    if n == 2:
        return 5 if 4 in counter.values() else 4
    if n == 3:
        return 3 if 3 in counter.values() else 2
    if n == 4:
        return 1
    return 0

hands = []
with open(FILENAME) as file:
    for line in file:
        hand, bet = line.strip().split(" ")
        hands.append((hand, int(bet)))

# This was generally copied from a mess of things.
# It turns out you don't need to order ties by top rank, but by card order ONLY.
hands.sort(key=lambda hand: (scoreHand(hand[0]), tuple([CARD_ORDER.index(c) for c in hand[0][:5]])))

# PART 1
print(sum(hand[1] * (i+1) for i, hand in enumerate(hands)))






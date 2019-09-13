# In Obedience to the Truth

# UVa 10205

import collections

Card = collections.namedtuple('Card', ['suit', 'value'])

ncards = 52
nvalues = 13
nsuits = 4

values = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
suits = [None, 'Clubs', 'Diamonds', 'Hearts', 'Spades']

def shuffle(cards, combination):
    cards_copy = cards.copy()
    for pos, card_idx in enumerate(combination[1:], 1):
        cards_copy[pos] = cards[card_idx]
    return cards_copy

deck = [0]
for s in suits[1:]:
    for v in values[1:]:
        deck.append(Card(s, v))

nc = int(input())
input()

for case in range(nc):
    ncombs = int(input())
    dck = list(range(ncards+1))
    combs = [None]
    card_set = []
    while len(card_set) < ncombs * ncards:
        card_set.extend(map(int, input().split()))


    for i in range(ncombs):
        e = i+1
        combs.append([0]+card_set[ncards*(e-1):ncards*e])

    while True:
        try:
            sh = input()
            if sh:
                sh = int(sh)
            else:
                break
            dck = shuffle(dck, combs[sh])
        except Exception:
            break

    for rank in dck[1:]:
        print(deck[rank].value, 'of', deck[rank].suit)

    if case == nc - 1:
        break
    print()

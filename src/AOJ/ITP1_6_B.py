import sys

cards = {
    "S": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "H": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "C": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
}

patterns = ['S', 'H', 'C', 'D']


def resolve():
    n = int(input())
    for card in sys.stdin:
        p, n = map(str, card.split())
        cards[p].remove(int(n))
    for pattern in patterns:
        for card in cards[pattern]:
            print("{} {}".format(pattern, card))

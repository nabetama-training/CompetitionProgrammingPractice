import sys


def print_cards(cards: [str]) -> [str]:
    print(''.join(cards))


def shuffle(h: int, cards: [str]) -> [str]:
    return cards[h:] + cards[:h]


def resolve():
    for line in sys.stdin:
        line = line[:-1]  # reduce \n
        if line == '-':
            break
        if line.isalpha():
            cards = list(line)
            m = int(input())
            for _ in range(m):
                h = int(input())
                cards = shuffle(h, cards=cards)
            print_cards(cards)

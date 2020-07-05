import sys


def resolve():
    for line in sys.stdin:
        x, y = map(int, line.split())
        if x == y == 0:
            break
        if x < y:
            print(x, y)
        else:
            print(y, x)
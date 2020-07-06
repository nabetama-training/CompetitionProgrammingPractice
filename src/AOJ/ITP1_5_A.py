import sys


def resolve():
    for line in sys.stdin:
        h, w = map(int, line.split())

        if h == w == 0:
            return

        for i in range(h):
            for j in range(w):
                print("#", end="")
            print()
        print()

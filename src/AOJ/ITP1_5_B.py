import sys


def resolve():
    for line in sys.stdin:
        h, w = map(int, line.split())

        if h == w == 0:
            return

        for i in range(h):
            if i == 0 or i == h - 1:
                for j in range(w):
                    print("#", end="")
            else:
                for j in range(w):
                    if j == 0 or j == w - 1:
                        print('#', end="")
                    else:
                        print('.', end="")
            print()
        print()


import sys


def resolve():
    for line in sys.stdin:
        h, w = map(int, line.split())

        if h == w == 0:
            return

        for i in range(h):
            if i % 2 == 0:
                for j in range(w):
                    if j % 2 == 0:
                        print('#', end='')
                    else:
                        print('.', end='')
            else:
                for j in range(w):
                    if j % 2 == 1:
                        print('#', end='')
                    else:
                        print('.', end='')
            print()
        print()

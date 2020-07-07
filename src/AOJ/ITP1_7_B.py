import sys


def ways(n: int, x: int) -> int:
    counter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    counter += 1
    return counter


def resolve():
    for line in sys.stdin:
        n, x = map(int, line.split())
        if n == x == 0:
            break

        print(ways(n, x))

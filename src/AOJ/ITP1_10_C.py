from functools import reduce


def resolve():
    while True:
        n = int(input())
        if n == 0:
            break
        ss = list(map(int, input().split()))

        m = sum(ss) / n
        a2 = reduce(lambda x, y: x + (y - m) ** 2, ss, 0)
        print((a2 / n) ** 0.5)

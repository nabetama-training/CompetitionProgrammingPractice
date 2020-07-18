#from functools import reduce


def resolve():
    _ = int(input())
    xv = list(map(float, input().split()))
    yv = list(map(float, input().split()))

    # for p in range(1, 4):
    #     print(reduce(lambda x, y: x + abs(y[0] - y[1]) ** p, zip(xv, yv), 0) ** (1 / p))

    # p = 1, 2, 3
    for p in range(1, 4):
        k = sum([abs(x - y) ** p for x, y in zip(xv, yv)]) ** (1 / p)
        print("{0:.8f}".format(k))
    # p = ∞
    print("{0:.8f}".format(max([abs(x - y) for x, y in zip(xv, yv)])))

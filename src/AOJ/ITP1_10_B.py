import math


def resolve():
    a, b, C = map(float, input().split())
    x = math.radians(C)

    h = b * math.sin(x)
    S = "{0:.8f}".format((a * h) / 2)
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(x))
    L = "{0:.8f}".format(a + b + c)
    print(S, L, h, sep="\n")

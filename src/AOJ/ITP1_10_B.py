import math
from decimal import Decimal, ROUND_HALF_UP


def resolve():
    a, b, C = map(int, input().split())
    x = math.radians(C)

    h = b * math.sin(x)
    S = Decimal((a * h) / 2).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)
    c = Decimal(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(x))).quantize(Decimal('0.00000001'),
                                                                               rounding=ROUND_HALF_UP)
    L = Decimal(a + b + c).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)
    print(S, L, h, sep="\n")

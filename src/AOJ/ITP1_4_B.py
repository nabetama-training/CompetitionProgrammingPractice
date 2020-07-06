from math import pi
from decimal import Decimal, ROUND_HALF_UP


def resolve():
    r = float(input())

    a = Decimal(r * r * pi).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
    c = Decimal(r * 2 * pi).quantize(Decimal('0.000010'), rounding=ROUND_HALF_UP)
    print(a, c)

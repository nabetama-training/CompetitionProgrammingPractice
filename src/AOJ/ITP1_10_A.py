import math
from decimal import Decimal, ROUND_HALF_UP


def resolve():
    x1, y1, x2, y2 = map(float, input().split())
    a = Decimal(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    print(a)

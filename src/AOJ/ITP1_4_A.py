from decimal import Decimal, ROUND_HALF_UP


def resolve():
    a, b = map(int, input().split())
    print(int(a / b), a % b, Decimal(str(a / b)).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP))

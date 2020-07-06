import sys


def calc(a: int, op: str, b: int) -> int:
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    return int(a / b)

def resolve():
    for line in sys.stdin:
        a, op, b = map(str, line.split())
        a = int(a)
        b = int(b)

        if op == '?':
            break

        # No using eval
        print(calc(int(a), op, int(b)))
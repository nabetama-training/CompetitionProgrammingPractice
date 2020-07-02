def mark(a: int, b: int) -> str:
    if a > b:
        return ">"
    if a < b:
        return "<"
    return "=="


def resolve():
    a, b = map(int, input().split())
    print("a {} b".format(mark(a, b)))

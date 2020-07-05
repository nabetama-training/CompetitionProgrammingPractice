def validate_x(w: int, x: int, r: int) -> bool:
    if r <= x <= w - r:
        return True
    return False


def validate_y(h: int, y: int, r: int) -> bool:
    if r <= y <= h - r:
        return True
    return False


def resolve():
    w, h, x, y, r = map(int, input().split())

    if validate_x(w, x, r) and validate_y(h, y, r):
        print("Yes")
    else:
        print("No")

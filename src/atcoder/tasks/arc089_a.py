from typing import Tuple


def is_reached_all(count: int, lines: int) -> bool:
    return count == lines


def is_reachable(t: int, x: int, y: int) -> Tuple[bool, int, int, int]:
    tt, xx, yy = map(int, input().split())
    if abs(x - xx) + abs(y - yy) <= tt - t and tt % 2 == (xx + yy) % 2:
        return True, tt, xx, yy
    return False, 0, 0, 0


def resolve():
    n = int(input())
    count = 0
    t, x, y = 0, 0, 0

    for _ in range(n):
        ok, t, x, y = is_reachable(t, x, y)
        if ok:
            count += 1

    if is_reached_all(count, n):
        print("Yes")
    else:
        print("No")

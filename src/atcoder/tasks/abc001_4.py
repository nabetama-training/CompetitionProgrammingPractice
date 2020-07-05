from typing import Tuple, List


def get_start(s: str) -> str:
    hh = s[:2]
    mm = int(s[2:])
    return "{}{}".format(hh, format(mm - mm % 5, '0>2'))


def get_end(s: str) -> str:
    hh = int(s[:2])
    mm = int(s[2:])

    over_min = mm % 5
    if 1 <= over_min < 5:
        e = mm + 5 - over_min
    else:
        e = mm

    if 60 <= e:
        hh += 1
        return "{}{}".format(format(hh, '0>2'), '00')
    return "{}{}".format(format(hh, '0>2'), format(e, '0>2'))


def time_idx_to_hhmm(idx: int) -> str:
    n = idx * 5
    hh = int(n / 60)
    mm = n % 60
    return "{}{}".format(format(hh, '0>2'), format(mm, '0>2'))


def resolve():
    n = int(input())

    # 24h * 60min を 5分ごとにしたリストを作る
    times = [0 for x in range(0, 1441, 5)]

    for _ in range(n):
        start, end = map(str, input().split('-'))
        s = get_start(start)
        e = get_end(end)

        s2 = int(s[:2]) * 60 + int(s[2:])
        e2 = int(e[:2]) * 60 + int(e[2:])

        for x in range(int(s2), int(e2), 5):
            times[int(x / 5)] = 1

    before = 0
    out = ''
    for i, flag in enumerate(times):
        if before != flag:
            out += time_idx_to_hhmm(i)
            before = flag
        if len(out) == 8:
            print("{}-{}".format(out[:4], out[4:]))
            out = ''

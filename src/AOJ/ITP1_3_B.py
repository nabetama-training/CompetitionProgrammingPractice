import sys


def resolve():
    idx = 1
    for num_s in sys.stdin:
        num = int(num_s)
        if num == 0:
            break
        print("Case {}: {}".format(idx, int(num)))
        idx += 1

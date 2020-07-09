import sys


def resolve():
    for x in sys.stdin:
        if int(x) == 0:
            break
        nums = [int(x) for x in list(x) if x != "\n"]
        print(sum(nums))

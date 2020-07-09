import sys


def resolve():
    alphabets = dict([(chr(c), 0) for c in range(ord('a'), ord('z') + 1)])

    for line in sys.stdin:
        for c in list(line):
            if c.isalpha():
                alphabets[c.lower()] += 1

    for k, v in alphabets.items():
        print("{} : {}".format(k, v))

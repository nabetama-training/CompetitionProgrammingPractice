import sys


def resolve():
    w = input()

    count = 0
    for line in sys.stdin:
        if line == "END_OF_TEXT\n":
            break

        words = map(lambda x: x.lower(), line.split())
        for word in words:
            if word == w:
                count += 1
    print(count)


# # In practice, I would write the following...
# def resolve2() -> int:
#     w = input()
#     print(sys.stdin.read().lower().split().count(w))

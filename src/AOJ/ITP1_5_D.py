def resolve():
    n = int(input())

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 10 == 3:
            print(" {}".format(i), end="")
        elif i % 3 == 0:
            print(" {}".format(i), end="")
        elif i % 10 == 3:
            print(" {}".format(i), end="")
        if i == n:
            print(" ")

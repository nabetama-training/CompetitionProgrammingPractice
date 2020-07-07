def resolve():
    # bills = [
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ],
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ],
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ],
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ],
    # ]

    bills = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

    n = int(input())
    for _ in range(n):
        b, f, r, v = map(int, input().split())
        bills[b - 1][f - 1][r - 1] += v

    count = 0
    for bill in bills:
        count += 1
        for floor in bill:
            [print(" {}".format(r), end='') for r in floor]
            print('')
        if count < len(bills):
            print('####################')

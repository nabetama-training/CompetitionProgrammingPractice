def resolve():
    n, y = map(int, input().split())

    if n * 1000 > y:
        print('-1 -1 -1')
        return

    for i in range(n + 1):  # 10000yen
        for j in range(n + 1 - i):  # 5000yen
            if 10000 * i + 5000 * j + 1000 * (n - i - j) == y:
                print(i, j, (n - i - j))
                return
    print('-1 -1 -1')

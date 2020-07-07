def resolve():
    n, m = map(int, input().split())
    a = []
    b = []

    for _ in range(n):
        a.append([int(s) for s in input().split()])

    for _ in range(m):
        b.append([int(input())])

    for i in range(n):
        s = 0
        for j in range(m):
            s += a[i][j] * b[j][0]
        print(s)

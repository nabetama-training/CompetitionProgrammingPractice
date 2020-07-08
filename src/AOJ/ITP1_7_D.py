def resolve():
    n, m, l = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    b = [list(map(int, input().split())) for i in range(m)]

    c = []

    for i in range(n):
        tmp = []
        for j in range(l):
            x = 0
            for k in range(m):
                x += a[i][k] * b[k][j]
            tmp.append(x)
        c.append(tmp)

    for line in c:
        print(*line)

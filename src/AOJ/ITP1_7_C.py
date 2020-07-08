def resolve():
    r, c = map(int, input().split())

    sum_c = [0 for _ in range(c)]
    for i in range(r):
        row = list(map(int, input().split()))
        for j, x in enumerate(row):
            print("{} ".format(x), end='')
            sum_c[j] += row[j]
        print(sum(row))

    [print("{} ".format(x), end="") for x in sum_c]
    print(sum(sum_c))

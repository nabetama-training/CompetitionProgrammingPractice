def resolve():
    n = int(input())

    ok = False
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                ok = True

    if ok:
        print("Yes")
    else:
        print("No")

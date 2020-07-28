def resolve():
    n = int(input())
    S = input()
    count = 0

    for i, s in enumerate(list(S)):
        if "ABC" == S[i:i + 3]:
            count += 1
    print(count)

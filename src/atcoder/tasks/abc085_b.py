def resolve():
    n = int(input())
    mochi = [int(input()) for _ in range(n)]
    print(len(set(mochi)))
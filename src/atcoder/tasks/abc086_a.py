# https://atcoder.jp/contests/abs/tasks/abc086_a
def resolve():
    a, b = list(map(int, input().split()))
    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")

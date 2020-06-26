# https://atcoder.jp/contests/abs/tasks/practice_1
def resolve():
    a = int(input())
    b, c = list(map(int, input().split()))
    d = input()
    print("{} {}".format(a + b + c, d))


resolve()

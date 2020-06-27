def my_sum(n):
    return sum(list(map(int, n)))


def resolve():
    n, a, b = list(map(int, input().split()))
    counter = 0

    for i in range(n + 1):
        if a <= my_sum(str(i)) <= b:
            counter += i
    print(counter)

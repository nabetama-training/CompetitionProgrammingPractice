def is_even_all(nums):
    return bool(len([x for x in nums if x % 2 == 0]) == len(nums))


def divide_all(nums):
    return [int(x / 2) for x in nums]


def resolve():
    counter = 0
    _ = int(input())
    nums = list(map(int, input().split()))
    while is_even_all(nums):
        nums = divide_all(nums)
        counter = counter + 1
    print(counter)

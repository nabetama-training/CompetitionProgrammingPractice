def isAllEven(nums):
    return bool(len([x for x in nums if x % 2 == 0]) == len(nums))


def divideAll(nums):
    return [int(x / 2) for x in nums]


def resolve():
    counter = 0
    _ = int(input())
    nums = list(map(int, input().split()))
    while isAllEven(nums):
        nums = divideAll(nums)
        counter = counter + 1
    print(counter)


resolve()

def resolve():
    _ = int(input())
    nums = list(map(int, input().split()))
    nums.reverse()  # destructive method

    counter = 1
    for num in nums:
        if counter == len(nums):
            print(num)
            break
        else:
            print(num, end=" ")
        counter += 1


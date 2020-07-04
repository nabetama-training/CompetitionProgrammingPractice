from typing import List


def resolve():
    print(" ".join(map(str, sorted(map(int, input().split())))))


def bubble_sort(numbers: List[int]) -> List[int]:
    if len(numbers) < 2:
        return numbers

    for i in range(len(numbers) - 1):
        left = 0
        right = 1

        while right < len(numbers):
            if numbers[left] > numbers[right]:
                numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right += 1
    return numbers


def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        # 1つ右の要素をソート対象にする
        j = i + 1

        # nums[j]がソート済みになるまで繰り返す
        while i >= 0:
            # nums[j]を一つ左の要素と比較し、nums[j]の方が小さければ交換する
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                # 比較対象が左に移動している
                i -= 1
                j -= 1
            else:
                break
    return nums

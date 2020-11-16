from typing import List

def list_reverser(nums: List[int]) -> None:
    start = 0
    end = len(nums) - 1

    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1    

A = [1, 2, 3, 4, 5, 6]
print(A)
list_reverser(A)
print("Reversed list is")
print(A)
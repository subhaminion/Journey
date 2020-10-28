# Given an array nums, 
# write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
from typing import List

def move_zeroes(nums: List[int]) -> None:
    anchor = 0
    for explorer in range(0, len(nums)):
        if nums[explorer] != 0:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor += 1

arr = [0,1,0,3,12]
move_zeroes(arr)
print(arr)
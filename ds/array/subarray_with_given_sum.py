# Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
# Examples :

# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Ouptut: Sum found between indexes 2 and 4
# Sum of elements between indices
# 2 and 4 is 20 + 3 + 10 = 33

# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Ouptut: Sum found between indexes 1 and 4
# Sum of elements between indices
# 1 and 4 is 4 + 0 + 0 + 3 = 7

# Input: arr[] = {1, 4}, sum = 0
# Output: No subarray found
# There is no subarray with 0 sum

# Time - O(n^2), Space - O(1)
def subarray_with_given_sum(arr, length, sum):
	for i in range(length):
		current_sum = arr[i]
		for j in range(i+1, length):
			if current_sum == sum:
				print(f"indexes {i} and {(j-1)}")
				return 1
			if current_sum > sum:
				break
			current_sum = current_sum + arr[j]
	print("nothing found")
	return 0

# Time - O(n), Space - O(1)
# Can't handle negative cases
def subarray_with_given_sum_o_n_complexity(arr, length, sum):
	current_sum = arr[0]
	start = 0
	for i in range(1, length):
		while current_sum > sum and start < length:
			current_sum = current_sum - arr[start]
			start += 1
		
		if current_sum == sum:
			print(f"indexes {start} and {(i-1)}")
			return 1

		current_sum = current_sum + arr[i]
	print('Not Found!')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
n = len(arr) 
sum = 6
  
subarray_with_given_sum(arr, n, sum)
subarray_with_given_sum_o_n_complexity(arr, n, sum)

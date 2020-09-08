# Approach: Count the number of 0s, 1s and 2s in the given array.
# Then store all the 0s in the beginning followed by all the 1s then all the 2s.
# Algorithm:
# Keep three counter c0 to count 0s, c1 to count 1s and c2 to count 2s
# Traverse through the array and increase the count of c0 is the element is 0, 
# increase the count of c1 is the element is 1 and increase the count of c2 is the element is 2
# Now again traverse the array and replace first c0 elements with 0, next c1 elements with 1 and next c2 elements with 2.

def sort_arr_0s_1s_2s(arr):
	count0 = count1 = count2 = 0
	length = len(arr)

	for i in range(length):
		if arr[i] == 0:
			count0 += 1
		
		elif arr[i] == 1:
			count1 +=1
		
		elif arr[i] == 2:
			count2 += 1

	i = 0
	while count0 > 0:
		arr[i] = 0
		i += 1
		count0 -= 1

	while count1 > 0:
		arr[i] = 1
		i += 1
		count1 -= 1

	while count2 > 0:
		arr[i] = 2
		i += 1
		count2 -= 1

	print(arr)


def sort_arr_0s_1s_2s_On(arr):
	low = mid = 0
	high = len(arr) - 1

	while(mid <= high):
		if (arr[mid] == 0):
			arr[low], arr[mid] = arr[mid], arr[low]
			low += 1
			mid += 1

		elif (arr[mid] == 1):
			mid += 1

		elif (arr[mid] == 2):
			arr[mid], arr[high] = arr[high], arr[mid]
			high -= 1
	print(arr)


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]   

# sort_arr_0s_1s_2s(arr) 
sort_arr_0s_1s_2s_On(arr)

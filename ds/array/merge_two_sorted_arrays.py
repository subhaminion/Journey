def merge(arr1, arr2):
	n1 = len(arr1)
	n2 = len(arr2)
	i = j = k = 0
	result = []
	while (i < n1 and j < n2):
		if arr1[i] < arr2[j]:
			result.append(arr1[i])
			i = i + 1
		else:
			result.append(arr2[j])
			j = j + 1

	while (i < n1):
		result.append(arr1[i])
		i = i + 1
	while (j < n2):
		result.append(arr2[j])
		j = j + 1

	print(result)

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merge(arr1, arr2)
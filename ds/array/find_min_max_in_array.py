def first_approach(arr):
    length = len(arr)
    if length == 1:
        min = arr[0]
        max = arr[0]
    
    if arr[0] > arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        min = arr[0]
        max = arr[1]
    
    for i in range(2, length):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    print(min, max)

def second_approach(arr):
    pass

# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    first_approach(arr)
def binarySearch(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, low, mid - 1, target)   # Left half
    else:
        return binarySearch(arr, mid + 1, high, target)  # Right half

arry = [1, 2, 3, 8, 9, 15]
target = 9

result = binarySearch(arry, 0, len(arry) - 1, target)

if result == -1:
    print("Element not found in the array")
else:
    print("Element found at:", result)

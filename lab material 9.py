def binarySearch(arr, key):
    arr.sort()   # Binary Search requires sorted array

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return f"Element {key} is found at position {mid+1}"

        elif arr[mid] < key:
            left = mid + 1

        else:
            right = mid - 1

    return f"Element {key} is not found"

# Tests
arr = [3,4,6,-9,10,8,9,30]
print(binarySearch(arr,10))
print(binarySearch(arr,100))

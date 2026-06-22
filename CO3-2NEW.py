def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid, count
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, count

arr = [1,2,3,4,5,6,7,8,9,10]
pos, iterations = binary_search(arr, 8)

print("Position:", pos)
print("Iterations:", iterations)

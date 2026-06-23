def findMax(arr):
    if not arr:
        return None

    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum

# Tests
print(findMax([1,2,3,4,5]))
print(findMax([7,7,7,7,7]))
print(findMax([-10,2,3,-4,5]))

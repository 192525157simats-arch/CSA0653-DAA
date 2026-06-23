def maxAfterSorting(arr):
    if not arr:
        return "List is empty"

    arr.sort()
    return arr[-1]

# Tests
print(maxAfterSorting([]))
print(maxAfterSorting([5]))
print(maxAfterSorting([3,3,3,3,3]))

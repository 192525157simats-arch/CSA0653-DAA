def uniqueElements(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

# Tests
print(uniqueElements([3,7,3,5,2,5,9,2]))
print(uniqueElements([-1,2,-1,3,2,-2]))
print(uniqueElements([1000000,999999,1000000]))

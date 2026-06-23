def findIntersectionValues(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = sum(1 for x in nums1 if x in set2)
    answer2 = sum(1 for x in nums2 if x in set1)

    return [answer1, answer2]

# Test
nums1 = [2,3,2]
nums2 = [1,2]
print(findIntersectionValues(nums1, nums2))

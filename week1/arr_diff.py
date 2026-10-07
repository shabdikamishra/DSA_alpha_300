class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = [x for x in set1 if x not in set2]
        diff2 = [x for x in set2 if x not in set1]

        return [diff1, diff2]
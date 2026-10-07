class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts= {}
        result= []

        #counting frequencies of elements
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        #matching against nums2 and decrease count
        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1

        return result
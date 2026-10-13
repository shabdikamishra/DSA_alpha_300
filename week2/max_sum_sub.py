class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = set()
        current_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            # if the current number already exists in window, shrink from left
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # add current number
            seen.add(nums[right])
            current_sum += nums[right]

            #if window exceeds size k, drop the leftmost number
            if right - left + 1 > k:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            #valid window of size k with all distinct elements
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
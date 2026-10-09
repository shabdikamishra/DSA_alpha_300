class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        n = len(arr)
        
        for i in range(0, n, 2 * k):
            left = i
            right = min(i + k - 1, n - 1)  # Reverse up to k chars or end of string
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
        return "".join(arr)
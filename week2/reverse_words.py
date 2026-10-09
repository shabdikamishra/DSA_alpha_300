class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        start = 0
        
        for i in range(n + 1):
            if i == n or arr[i] == ' ':
                left = start
                right = i - 1
                while left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
                start = i + 1
                
        return "".join(arr)
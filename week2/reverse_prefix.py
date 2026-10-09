class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)
        idx = -1
        
        for i in range(len(arr)):
            if arr[i] == ch:
                idx = i
                break
                
        if idx != -1:
            left, right = 0, idx
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
        return "".join(arr)
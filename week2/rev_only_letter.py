class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        left, right= 0, len(arr) - 1
        
        while left < right:
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
                
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left+= 1
                right-= 1
                
        return "".join(arr)
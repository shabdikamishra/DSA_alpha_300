class Solution:
    def reverseWords(self, s: str) -> str:
        # full sentence reversal
        #extract words manually without relying on high-level splits
        words = []
        n = len(s)
        i = 0
        
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[start:i])
            
        #reverse the array of word tokens
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
            
        return " ".join(words)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        def expand(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        for i in range(n):
            # Odd length palindromes
            count += expand(i, i)
            # Even length palindromes
            count += expand(i, i + 1)
            
        return count
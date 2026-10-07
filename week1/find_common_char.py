class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Count characters in the first word
        common = {}
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1

        # Keep minimum frequency across all other words
        for word in words[1:]:
            curr = {}
            for ch in word:
                curr[ch] = curr.get(ch, 0) + 1

            for ch in list(common.keys()):
                if ch in curr:
                    common[ch] = min(common[ch], curr[ch])
                else:
                    del common[ch]

        res = []
        for ch, count in common.items():
            res.extend([ch] * count)

        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        high = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            high = max(high, count[s[r]])
            while (r - l + 1) - high > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
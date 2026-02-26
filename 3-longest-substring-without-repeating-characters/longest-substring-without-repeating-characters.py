class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = Counter()
        
        maxLen = 0
        l = 0

        for r in range(len(s)):
            while unique[s[r]] > 0:
                unique[s[l]] -= 1
                l += 1
            unique[s[r]] += 1

            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
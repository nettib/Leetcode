class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        long_substring = 1
        l = 0
        for r in range(1, len(s)):
            while l < r and s[r] in s[l:r]:
                l += 1
            long_substring = max(long_substring, r - l + 1)
        return long_substring
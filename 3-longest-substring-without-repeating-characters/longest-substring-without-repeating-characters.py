class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            unique.add(s[r])

        return longest
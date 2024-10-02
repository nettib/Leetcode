class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        arr = []
        longest = 1
        for r in range(0, len(s)):
            while s[r] in arr:
                if len(arr) != 0:
                    arr.remove(arr[0])
                    longest = max(longest, len(arr))
            arr.append(s[r])
            longest = max(longest, len(arr))
        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # unique = set()
        # longest = 0

        # l = 0
        # for r in range(len(s)):
        #     while s[r] in unique:
        #         unique.remove(s[l])
        #         l += 1
        #     longest = max(longest, r - l + 1)
        #     unique.add(s[r])

        # return longest
        seen = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            curr_char = s[end]
            if curr_char in seen and seen[curr_char] >= start:
                start = seen[curr_char] + 1
            seen[curr_char] = end
            max_len = max(max_len, end - start + 1)
        return max_len
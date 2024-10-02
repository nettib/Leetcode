class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store characters in the current window
        left = 0  # Left pointer
        longest = 0  # Length of the longest substring

        for right in range(len(s)):
            # If we encounter a duplicate, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length found
            longest = max(longest, right - left + 1)

        return longest
        
        # if len(s) == 0:
        #     return 0
        # arr = []
        # longest = 1
        # for r in range(0, len(s)):
        #     while s[r] in arr:
        #         if len(arr) != 0:
        #             arr.remove(arr[0])
        #             longest = max(longest, len(arr))
        #     arr.append(s[r])
        #     longest = max(longest, len(arr))
        # return longest
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        track = set()
        maxSub = 0
        l = 0

        for r in range(len(s)):

            while s[r] in track:
                if s[l] in track:
                    track.remove(s[l])
                l += 1

            track.add(s[r])
            maxSub = max(maxSub, r - l + 1)
        
        return maxSub
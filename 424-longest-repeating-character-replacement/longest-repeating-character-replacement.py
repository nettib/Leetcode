class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        track = {}
        maxF = -float("inf")
        longChar = -float("inf")
        l = 0

        for r in range(len(s)):
            track[s[r]] = track.get(s[r], 0) + 1
            maxF = max(maxF, track[s[r]])

            while (r - l) - maxF >= k:
                track[s[l]] -= 1
                l += 1
            
            longChar = max(longChar, r - l + 1)
        
        return longChar
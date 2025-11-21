class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        track = {}
        longChar = -float("inf")
        l = 0

        for r in range(len(s)):
            track[s[r]] = track.get(s[r], 0) + 1

            while (r - l) - max(track.values()) == k:
                track[s[l]] -= 1
                l += 1
            
            longChar = max(longChar, r - l + 1)
        
        return longChar
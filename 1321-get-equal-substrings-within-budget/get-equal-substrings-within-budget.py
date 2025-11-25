class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l = 0
        maxLen = 0
        currCost = 0

        for r in range(len(s)):
            currCost += abs(ord(s[r]) - ord(t[r]))

            while l <= r and currCost > maxCost:
                currCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            if l <= r:
                maxLen = max(maxLen, r - l + 1)
        
        return maxLen

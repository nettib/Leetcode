class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sHash = {}
        tHash = {}

        for i in range(len(t)):
            tHash[t[i]] = tHash.get(t[i], 0) + 1
            if t[i] not in sHash:
                sHash[t[i]] = 0
        
        have = 0
        need = len(tHash)
        minSub = [0, float("inf")]

        l = 0
        for r in range(len(s)):
            if s[r] in sHash:
                sHash[s[r]] += 1
                if sHash[s[r]] == tHash[s[r]]:
                    have += 1
            
            while l <= r and have == need:
                if (minSub[-1] - minSub[0]) > (r - l):
                    minSub[-1], minSub[0] = r, l
                
                if s[l] in sHash:
                    sHash[s[l]] -= 1
                    if sHash[s[l]] < tHash[s[l]]:
                        have -= 1
                
                l += 1
        
        if minSub[-1] == float("inf"):
            return ""
        
        return s[minSub[0]: minSub[-1] + 1]

                

        

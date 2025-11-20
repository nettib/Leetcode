class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1Hash = {}
        s2Hash = {}

        for i in range(len(s1)):
            s1Hash[s1[i]] = s1Hash.get(s1[i], 0) + 1

        have = 0
        need = len(s1Hash)
        for i in range(len(s1)):
            s2Hash[s2[i]] = s2Hash.get(s2[i], 0) + 1
            if s2[i] in s1Hash and s2Hash[s2[i]] == s1Hash[s2[i]]:
                have += 1
        
        if have == need:
            return True
        
        for i in range(len(s1), len(s2)):
            if s2[i - len(s1)] in s1Hash and s2Hash[s2[i - len(s1)]] == s1Hash[s2[i - len(s1)]]:
                have -= 1
            s2Hash[s2[i - len(s1)]] -= 1
            if s2Hash[s2[i - len(s1)]] == 0:
                del s2Hash[s2[i - len(s1)]]
            s2Hash[s2[i]] = s2Hash.get(s2[i], 0) + 1
            if s2[i] in s1Hash and s2Hash[s2[i]] == s1Hash[s2[i]]:
                have += 1
            if have == need:
                return True
        
        return False


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp1 = {}
        mapp2 = {}

        for i in range(len(s)):
            if s[i] in mapp1:
                if mapp1[s[i]] != t[i]:
                    return False
            else:
                mapp1[s[i]] = t[i]

        for i in range(len(t)):
            if t[i] in mapp2:
                if mapp2[t[i]] != s[i]:
                    return False
            else:
                mapp2[t[i]] = s[i]

        
        return True
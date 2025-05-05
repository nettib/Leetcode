class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_hash = {}
        p_hash = {}
        k = len(p)
        res = []

        if k > len(s):
            return res

        for i in range(k):
            if p[i] in p_hash:
                p_hash[p[i]] += 1
            else:
                p_hash[p[i]] = 1
        
        for i in range(k):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1
            
        if s_hash == p_hash:
            res.append(0)

        for i in range(k, len(s)):
            s_hash[s[i - k]] -= 1
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1

            if s_hash[s[i - k]] == 0:
                del s_hash[s[i - k]]

            if s_hash == p_hash:
                res.append((i - k) + 1)

        return res
        
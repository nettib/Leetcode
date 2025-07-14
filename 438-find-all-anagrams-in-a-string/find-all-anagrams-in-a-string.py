class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_hash = {}
        s_hash = {}

        res = []

        for char in p:
            if char not in p_hash:
                p_hash[char] = 0
            p_hash[char] += 1

        for i in range(len(p)):
            if s[i] not in s_hash:
                s_hash[s[i]] = 0
            s_hash[s[i]] += 1

        if s_hash == p_hash:
            res.append(0)

        for i in range(len(p), len(s)):
            if s_hash[s[i - len(p)]] == 1:
                del s_hash[s[i - len(p)]]
            else:
                s_hash[s[i - len(p)]] -= 1
            
            if s[i] not in s_hash:
                s_hash[s[i]] = 0
            s_hash[s[i]] += 1

            if s_hash == p_hash:
                res.append(i - len(p) + 1)
        
        return res
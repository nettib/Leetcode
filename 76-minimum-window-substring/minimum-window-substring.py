class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_hash = {}
        t_hash = {}

        for char in t:
            t_hash[char] = t_hash.get(char, 0) + 1

        have, need = 0, len(t_hash)
        res = None

        l = 0
        for r in range(len(s)):
            if s[r] in t_hash:
                s_hash[s[r]] = s_hash.get(s[r], 0) + 1
                if s_hash[s[r]] == t_hash[s[r]]:
                    have += 1
                while have == need:
                    if res == None or len(s[l:r + 1]) < len(res):
                        res = s[l:r + 1]
                    if s[l] in s_hash:
                        s_hash[s[l]] -= 1
                        if s_hash[s[l]] < t_hash[s[l]]:
                            have -= 1
                    l += 1

        return res if res else ""


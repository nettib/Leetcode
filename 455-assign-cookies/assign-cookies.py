class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        l = r = 0
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                res += 1
                l += 1
                r += 1
            else:
                r += 1
        return res

        

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        p1 = p2 = 0
        while p1 < len(s):
            if p2 < len(spaces) and p1 == spaces[p2]:
                res += " "
                p2 += 1
            else:
                res += s[p1]
                p1 += 1

        return res


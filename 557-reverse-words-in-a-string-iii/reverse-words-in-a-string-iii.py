class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        l = 0
        for r in range(len(s)):
            if s[r] == " ":
                res += s[l:r][::-1]
                res += s[r]
                l = r + 1
        res += s[l:r + 1][::-1]
        return res


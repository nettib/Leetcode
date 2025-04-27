class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        l = 0
        for r in range(len(s)):
            if s[r] == " ":
                ans += s[l: r][::-1]
                ans += s[r]
                l = r + 1
        ans += s[l:][::-1]
        return ans



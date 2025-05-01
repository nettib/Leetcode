class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            temp = ""
            if s[l] != s[r]:
                return r - l + 1
            else:
                temp = s[l]
            while l < r and s[l] == temp:
                l += 1
            while l < r and s[r] == temp:
                r -= 1
            if l == r and s[l] == temp:
                return 0

        return 1



        
            
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a = a[::-1]
        st = " ".join(a)

        return st
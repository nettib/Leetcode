class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def basic(num,b):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num%b))
                num//=b
            return "".join(digits[::-1])
        for i in range(2,n-1):
            pal = basic(n,i)
            if pal != pal[::-1]:
                return False
        return True


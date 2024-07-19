class Solution:
    def isPalindrome(self, s: str) -> bool:
        chr=""
        for char in s:
            if char.isalnum():
                chr=chr+char
        chr=chr.lower()
        lp=0
        rp=len(chr)-1
        while(lp<rp):
            if chr[lp]!=chr[rp]:
                return False
            lp+=1
            rp-=1
        return True
        

        
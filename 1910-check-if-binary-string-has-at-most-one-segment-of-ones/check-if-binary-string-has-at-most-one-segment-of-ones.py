class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = 0

        for i in range(len(s)):
            if s[i] == '1':
                if i == 0:
                    ones += 1
                elif s[i - 1] != '1' and ones:
                    return False
            
        return True

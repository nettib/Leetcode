class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = 0
        count2 = 0
        vowels = "aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowels:
                if i < len(s) / 2:
                    count1 += 1
                else:
                    count2 += 1
        return count1 == count2

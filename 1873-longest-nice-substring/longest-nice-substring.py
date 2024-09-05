class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        @cache
        def isNiceSubString(substring):
            charSet = set(substring)
            for char in substring:
                if char.swapcase() not in charSet:
                    return False
            return True
        longestNice = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                current = s[i:j+1]
                if isNiceSubString(current):
                    if len(current) > len(longestNice):
                        longestNice = current
        return longestNice
        
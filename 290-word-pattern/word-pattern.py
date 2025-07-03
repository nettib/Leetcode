class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted_str = s.split(" ")

        if len(pattern) != len(splitted_str):
            return False

        matchS1 = {}
        matchS2 = {}

        for i in range(len(pattern)):
            if pattern[i] in matchS1 and matchS1[pattern[i]] != splitted_str[i]:
                return False
            matchS1[pattern[i]] = splitted_str[i]

        for i in range(len(splitted_str)):
            if splitted_str[i] in matchS2 and matchS2[splitted_str[i]] != pattern[i]:
                return False
            matchS2[splitted_str[i]] = pattern[i]

        return True
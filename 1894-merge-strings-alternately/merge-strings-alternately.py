class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        p1 = 0
        p2 = 0
        flag = 0
        while p1 < len(word1) and p2 < len(word2):
            if flag == 0:
                merged += word1[p1]
                p1 += 1
                flag = 1
            else:
                merged += word2[p2]
                p2 += 1
                flag = 0
        if p1 < len(word1):
            merged += word1[p1:]
        if p2 < len(word2):
            merged += word2[p2:]

        return merged
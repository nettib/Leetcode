class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for i in word1:
            w1+=i
        for j in word2:
            w2+=j
        return w1==w2
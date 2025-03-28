class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def to_num(word):
            return int(''.join(str(ord(c) - ord('a')) for c in word))
        return to_num(firstWord) + to_num(secondWord) == to_num(targetWord)
        
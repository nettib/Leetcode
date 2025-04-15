class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        track = True
        for i in range(len(words)):
            l, r = 0, len(words[i]) - 1
            while l <= r:
                if words[i][l] != words[i][r]:
                    track = False
                    break
                l += 1
                r -= 1
            if track:
                return words[i]
            else:
                track = True
        return ""
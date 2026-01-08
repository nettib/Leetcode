class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        track = {}
        maxLen = -1

        for i in range(len(s)):
            if s[i] not in track:
                track[s[i]] = i
            else:
                maxLen = max(maxLen, (i - track[s[i]]) - 1)
        
        return maxLen
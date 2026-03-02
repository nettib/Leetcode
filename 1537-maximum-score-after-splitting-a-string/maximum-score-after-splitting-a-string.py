class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = []

        score = 0

        curr = 0
        for char in s:
            if char == "1":
                curr += 1
            ones.append(curr)
        
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            score = max(score, (ones[-1] - ones[i]) + zeros)
        
        return score
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = { "T": 0, "F": 0 }
        max_confuse = 0

        l = 0
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1

            while min(count.values()) > k:
                count[answerKey[l]] -= 1
                l += 1
                
            max_confuse = max(max_confuse, r - l + 1)
        
        return max_confuse
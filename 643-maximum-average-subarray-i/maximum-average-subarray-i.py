class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -float("inf")
        curr = 0

        for i in range(k):
            curr += nums[i]
        
        max_sum = max(max_sum, curr)

        for i in range(k, len(nums)):
            curr -= nums[i - k]
            curr += nums[i]

            max_sum = max(max_sum, curr)
        
        return max_sum / k
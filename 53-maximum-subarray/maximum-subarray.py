class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curr = 0

        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            maxSub = max(maxSub, curr)
        
        return maxSub
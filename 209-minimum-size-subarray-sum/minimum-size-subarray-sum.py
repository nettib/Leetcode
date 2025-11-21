class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minSize = float("inf")
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minSize = min(minSize, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if minSize == float("inf") else minSize
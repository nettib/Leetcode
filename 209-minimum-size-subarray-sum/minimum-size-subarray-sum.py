class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sub = float("inf")
        total = 0

        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_sub = min(min_sub, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if min_sub == float("inf") else min_sub
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        l = 0
        r = l + (k - 1)
        min_diff = float("inf")
        while r < len(nums):
            diff = nums[r] - nums[l]
            min_diff = min(min_diff, diff)
            l += 1
            r += 1
        return min_diff
    
        

        
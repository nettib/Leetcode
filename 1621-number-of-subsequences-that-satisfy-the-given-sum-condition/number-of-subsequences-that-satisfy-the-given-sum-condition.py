class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        m = (10 ** 9) + 7
        ans = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += (2 ** (r - l))
                ans = ans % m
                l += 1
        return ans 


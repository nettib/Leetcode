class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = l + 1
        while r < len(nums):
            if nums[l] == nums[r]:
                l = r + 1
                r = l + 1
            else:
                return nums[l]
        return nums[len(nums) - 1]
        

        
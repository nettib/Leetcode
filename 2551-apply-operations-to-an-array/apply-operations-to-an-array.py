class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums
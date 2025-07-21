class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        if nums[len(nums) - 1] - nums[0] == 0:
            return 0
        
        for i in range(1, len(nums) - 1):
            if nums[len(nums) - 1] - nums[i] == nums[i - 1]:
                return i
        
        if nums[len(nums) - 2] == 0:
            return len(nums) - 1
        
        return -1
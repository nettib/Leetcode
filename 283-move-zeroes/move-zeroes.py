class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p = 0
    
        for s in range(len(nums)):
            if nums[s] != 0:
                nums[s], nums[p] = nums[p], nums[s]
                p += 1
            
        return nums
            
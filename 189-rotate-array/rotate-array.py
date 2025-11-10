class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def rotateArray(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        

        rotateArray(0, len(nums) - 1)
        rotateArray(0, k - 1)
        rotateArray(k, len(nums) - 1)
        
        
        return nums

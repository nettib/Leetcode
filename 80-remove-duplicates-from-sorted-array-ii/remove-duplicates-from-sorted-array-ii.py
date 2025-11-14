class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                flag = 0
                nums[l] = nums[r]
                l += 1
            elif flag == 0:
                flag += 1
                nums[l] = nums[r]
                l += 1
        
        return l
        
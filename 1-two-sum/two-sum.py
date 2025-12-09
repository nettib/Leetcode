class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        track = {}

        for i in range(len(nums)):
            if target - nums[i] in track:
                return [track[target - nums[i]], i]
            else:
                track[nums[i]] = i
        

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        track = { 0: 0, 1: 0 }
        l = 0
        maxLen = 0

        for r in range(len(nums)):
            track[nums[r]] += 1

            while l <= r and track[0] > k:
                track[nums[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
        
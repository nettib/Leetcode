class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        longestGood = 0

        l = 0
        for r in range(len(nums)):
            while nums[r] in freq and freq[nums[r]] == k:
                freq[nums[l]] = freq.get(nums[l], 0) - 1
                l += 1

            freq[nums[r]] = freq.get(nums[r], 0) + 1
            longestGood = max(longestGood, r - l + 1)
        
        return longestGood
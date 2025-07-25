class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = [0] *(len(nums))

        count = 1
        prefix = nums[0]
        for i in range(1, len(nums)):
            res[i] = (count * nums[i]) - prefix
            count += 1
            prefix += nums[i]
        
        count = 1
        postfix = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] += postfix - (count * nums[i])
            count += 1
            postfix += nums[i]
        
        return res

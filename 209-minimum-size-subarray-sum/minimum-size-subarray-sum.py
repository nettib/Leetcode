class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currentSum = 0
        minLength = float("inf")
        for right in range(len(nums)):
            currentSum+=nums[right]
            while currentSum>= target:
                minLength = min(minLength,right-left+1)
                currentSum -=nums[left]
                left+=1
        if minLength == float("inf"):
            return 0
        else:
            return minLength


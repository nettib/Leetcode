class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        maxSum = current_sum
        for i in range(k,len(nums)):
            current_sum = current_sum + nums[i]
            current_sum = current_sum - nums[i-k]
            maxSum = max(maxSum,current_sum)
        return maxSum/k
        
        
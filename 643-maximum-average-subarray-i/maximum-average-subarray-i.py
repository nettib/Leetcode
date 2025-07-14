class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        total = current

        for i in range(k, len(nums)):
            current -= nums[i - k]
            current += nums[i]
            if current > total:
                total = current
        
        return total / k
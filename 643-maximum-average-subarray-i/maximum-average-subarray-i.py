class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = sum(nums[:k])
        current_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            current_sum -= nums[i - k]
            current_sum += nums[i]
            mx = max(mx, current_sum)
        
        return mx / k


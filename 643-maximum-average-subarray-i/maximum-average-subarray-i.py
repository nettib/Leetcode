class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        mx = current
        for i in range(k,len(nums)):
            current+=nums[i]
            current-=nums[i-k]
            mx = max(mx,current)
        return mx / k
        
        
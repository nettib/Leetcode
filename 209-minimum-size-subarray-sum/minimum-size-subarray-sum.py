class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current = 0
        min_size = float("inf")

        for r in range(len(nums)):
            current += nums[r]
            if current >= target:
                min_size = min(min_size, r - l + 1)
            while current >= target:
                current -= nums[l]
                l += 1
                if current >= target:
                    min_size = min(min_size, r - l + 1)
        
        if min_size == float("inf"):
            return 0
        return min_size



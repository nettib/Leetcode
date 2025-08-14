class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        swaps = 0
        min_swaps = 0

        for i in range(total):
            if nums[i] == 0:
                swaps += 1
                min_swaps = swaps
        
        for i in range(total, len(nums) * 2):
            if nums[(i - total) % len(nums)] == 0:
                swaps -= 1
            if nums[i % len(nums)] == 0:
                swaps += 1
            min_swaps = min(min_swaps, swaps)

        return min_swaps
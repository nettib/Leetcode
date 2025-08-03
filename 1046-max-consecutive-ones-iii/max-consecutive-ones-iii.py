class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        flag = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flag += 1
            while flag > k:
                if nums[l] == 0:
                    flag -= 1
                l += 1
            max_ones = max(max_ones, r - l + 1)
        
        return max_ones
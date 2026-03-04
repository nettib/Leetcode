class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sliding_window(nums, goal):
            count = 0

            curr = 0
            l = 0
            for r in range(len(nums)):
                curr += nums[r]

                while l < r and curr > goal:
                    curr -= nums[l]
                    l += 1
                
                if curr <= goal:
                    count += (r - l + 1)
            
            return count
            
        return sliding_window(nums, goal) - sliding_window(nums, goal - 1)

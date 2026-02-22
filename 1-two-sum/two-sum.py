class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_track = {}

        for i, num in enumerate(nums):
            if target - num in nums_track:
                return [nums_track[target - num], i]
            else:
                nums_track[num] = i
        
        
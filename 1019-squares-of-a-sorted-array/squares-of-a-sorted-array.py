class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for s in range(len(nums)):
            nums[s]=(nums[s])**2
        nums.sort()
        return nums
        
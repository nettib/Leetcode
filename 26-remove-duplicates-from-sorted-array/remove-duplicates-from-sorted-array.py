class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=left+1
        while right<len(nums):
            if nums[left]==nums[right]:
                nums.remove(nums[right])
            else:
                left=right
                right+=1
        return len(nums)
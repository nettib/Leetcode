class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if l < len(nums) and nums[r] != val and nums[l] == val and l < r:
                nums[l], nums[r] = nums[r], nums[l]
            while l < len(nums) and nums[l] != val:
                l += 1
        return l


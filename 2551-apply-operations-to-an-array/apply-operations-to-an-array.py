class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    nums[i] = nums[i] * 2
                    nums[i + 1] = 0
            for j in nums:
                if j==0:
                    nums.remove(j)
                    nums.append(j)
            return nums
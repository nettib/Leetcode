class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            target = nums[i]
            count = 0
            for j in nums:
                if j < target:
                    count += 1
            output.append(count)
        return output
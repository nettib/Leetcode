class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i == 0:
                dic[sorted_nums[i]] = i
            elif sorted_nums[i] != sorted_nums[i - 1]:
                dic[sorted_nums[i]] = i
            else:
                continue
        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        return nums


        
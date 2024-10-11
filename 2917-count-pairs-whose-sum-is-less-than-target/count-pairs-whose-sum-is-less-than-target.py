class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        left = 0
        right = left + 1
        while left < len(nums) - 1:
            if nums[left] + nums[right] < target:
                count+=1
            if right == len(nums) - 1:
                left+=1
                right = left + 1
            elif right != len(nums) - 1:
                right+=1
        return count


        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < target:
        #             count+=1
        # return count

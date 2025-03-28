class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = global_max = nums[0]
        partition = 0
        for i in range(1, len(nums)):
            global_max = max(global_max, nums[i])
            if nums[i] < left_max:
                left_max = global_max
                partition = i
        return partition + 1
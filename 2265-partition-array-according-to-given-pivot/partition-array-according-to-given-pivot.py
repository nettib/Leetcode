class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        equal = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                small.append(nums[i])
            elif nums[i] > pivot:
                large.append(nums[i])
            else:
                equal.append(nums[i])
        nums = small + equal + large
        return nums
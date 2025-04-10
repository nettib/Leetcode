class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [0] * len(nums)
        i1 = 0
        j1 = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] < pivot:
                res[i1] = nums[i]
                i1 += 1
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > pivot:
                res[j1] = nums[j]
                j1 -= 1
        for k in range(i1, j1 + 1):
            res[k] = pivot
        
        return res







        # small = [] 
        # large = []
        # equal = []
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         small.append(nums[i])
        #     elif nums[i] > pivot:
        #         large.append(nums[i])
        #     else:
        #         equal.append(nums[i])
        # nums = small + equal + large
        # return nums
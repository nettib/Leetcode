class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s, e = 0, len(nums) - 1
        res = [-1, -1]

        while s <= e:
            m = s + ((e - s) // 2)
            if nums[m] > target:
                e = m - 1
            else:
                if nums[m] == target:
                    res[-1] = m
                s = m + 1
        
        s, e = 0, len(nums) - 1
        while s <= e:
            m = s + ((e - s) // 2)
            if nums[m] < target:
                s = m + 1  
            else:
                if nums[m] == target:
                    res[0] = m
                e = m - 1 

        return res
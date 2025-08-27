class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        minm = min(nums[l], nums[r])

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > minm:
                l = m + 1
            else:
                minm = nums[m]
                r = m - 1
        
        return minm
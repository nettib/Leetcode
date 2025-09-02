# Testcase [1] 0
class Solution:
    def binarySearch(self, nums, l, r, target):
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return -1
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return self.binarySearch(nums, l, r, target)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        
        pi = l
        pf = l - 1
        print(pi, pf)

        if target >= nums[0] and target <= nums[pf]:
            return self.binarySearch(nums, 0, pf, target)
        elif target >= nums[pi] and target <= nums[-1]:
            return self.binarySearch(nums, pi, len(nums) - 1, target)
        else:
            return -1




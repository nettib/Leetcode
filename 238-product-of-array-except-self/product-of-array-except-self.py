class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = nums[:]
        arr2 = nums[::-1]

        for i in range(1, len(arr1)):
            arr1[i] *= arr1[i - 1]
            arr2[i] *= arr2[i - 1]
        
        arr2 = arr2[::-1]
        
        nums[0] = arr2[1]
        nums[len(nums) - 1] = arr1[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            nums[i] = arr1[i - 1] * arr2[i + 1]

        return nums
        

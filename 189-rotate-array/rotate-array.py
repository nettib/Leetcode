class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        flag = 0
        while flag < k:
            nums.insert(0,nums[len(nums)-1])
            nums.pop()
            flag+=1

        """
        Do not return anything, modify nums in-place instead.
        """
        
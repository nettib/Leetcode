class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k is greater than the length of the array

        # Helper function to reverse a portion of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements
        reverse(0, k - 1)

        # Step 3: Reverse the rest of the array
        reverse(k, n - 1)

        # for i in range(0,k):
        #     nums.insert(0,nums[len(nums)-1])
        #     nums.pop()










        # flag = 0
        # while flag < k:
        #     nums.insert(0,nums[len(nums)-1])
        #     nums.pop()
        #     flag+=1

        """
        Do not return anything, modify nums in-place instead.
        """
        
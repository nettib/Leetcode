class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * len(nums)

        stack = []

        for i in range(n):

            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]

            stack.append(i)

        for i in range(n):

            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                if result[index] == -1:
                    result[index] = nums[i]

            stack.append(i)

        return result

        
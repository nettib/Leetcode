class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                if nums2[index] in nums1:
                    result[nums1.index(nums2[index])] = nums2[i]

            stack.append(i)

        return result
            
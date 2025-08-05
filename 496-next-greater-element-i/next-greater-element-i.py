class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxMap = {}
        stack = []

        for i, num in enumerate(nums1):
            idxMap[num] = i

        nums1 = [-1] * len(nums1)

        for i in range(0, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                nums1[idxMap[stack.pop()]] = nums2[i]
            
            if nums2[i] in idxMap:
                stack.append(nums2[i])

        return nums1

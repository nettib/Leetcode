class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = { num: i for i, num in enumerate(nums1) }

        stack = []
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                res[track[val]] = nums2[i]
            if nums2[i] in track:
                stack.append(nums2[i])
        
        return res
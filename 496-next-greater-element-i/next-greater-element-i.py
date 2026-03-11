class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                next_greater[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        ans = [-1] * len(nums1)

        for i in range(len(nums1)):
            if nums1[i] in next_greater:
                ans[i] = next_greater[nums1[i]]
        
        return ans








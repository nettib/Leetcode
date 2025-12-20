class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = { num: i for i, num in enumerate(nums1) }
        ans = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                num = stack.pop()
                if num in track:
                    ans[track[num]] = nums2[i]
            stack.append(nums2[i])
        
        return ans
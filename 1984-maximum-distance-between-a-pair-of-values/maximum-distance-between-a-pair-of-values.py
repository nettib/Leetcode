class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        max_dist = 0
        while i < len(nums1) and j < len(nums2):
            if i <= j and nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            elif i < j and nums1[i] > nums2[j]:
                i += 1
            else:
                i += 1
                j += 1
                
        return max_dist
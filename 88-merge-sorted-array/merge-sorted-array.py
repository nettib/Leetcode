class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        if n != 0:
            l, r = m - 1, n - 1
            position = (m + n) - 1
            while l >= 0 and r >= 0:
                if nums1[l] >= nums2[r]:
                    nums1[position] = nums1[l]
                    l -= 1
                else:
                    nums1[position] = nums2[r]
                    r -= 1
                position -= 1
            
            while r >= 0:
                nums1[position] = nums2[r]
                r -= 1
                position -= 1



            
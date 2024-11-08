class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        k = m + n - 1
        while left >= 0 and right >= 0:
            if nums2[right] > nums1[left]:
                nums1[k] = nums2[right]
                right-=1
                k-=1
            elif nums1[left] >= nums2[right]:
                nums1[k] = nums1[left]
                left-=1
                k-=1
        while right >= 0:
            nums1[k] = nums2[right]
            right-=1
            k-=1
        # while left >= 0:
        #     nums1[k] = nums1[left]
        #     left-=1
        #     k-=1





        # arr = []
        # if m == 0:
        #     for i in range(len(nums2)):
        #         nums1[i] = nums2[i]
        # elif m!= 0 and n!=0:
        #     left = 0
        #     right = 0
        #     while left < m and right < n:
        #         if nums1[left] <= nums2[right]:
        #             arr.append(nums1[left])
        #             left+=1
        #         elif nums1[left] > nums2[right]:
        #             arr.append(nums2[right])
        #             right+=1
        #     while right < n:
        #         arr.append(nums2[right])
        #         right+=1
        #     while left < m:
        #         arr.append(nums1[left])
        #         left+=1
        #     for i in range(len(arr)):
        #         nums1[i] = arr[i]




       
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = []
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        elif m!= 0 and n!=0:
            left = 0
            right = 0
            while left < m and right < n:
                if nums1[left] <= nums2[right]:
                    arr.append(nums1[left])
                    left+=1
                elif nums1[left] > nums2[right]:
                    arr.append(nums2[right])
                    right+=1
            while right < n:
                arr.append(nums2[right])
                right+=1
            while left < m:
                arr.append(nums1[left])
                left+=1
            for i in range(len(arr)):
                nums1[i] = arr[i]




        # if m == 0:
        #     for i in range(len(nums2)):
        #         nums1[i] = nums2[i]
        # elif m!= 0 and n!=0:
        #     left = 0
        #     right = 0
        #     while left < m and right < n:
        #         if nums1[left] <= nums2[right]:
        #             left+=1
        #         elif nums1[left] > nums2[right]:
        #             temp = nums1[left]
        #             nums1[left] = nums2[right]
        #             left+=1
        #             right+=1
        #             nums1[left] = temp
        #             m+=1
        #     if right < n:
        #         for i in range(left,len(nums1)):
        #             nums1[i] = nums2[right]
        #             right+=1
        #     if left < m:
                

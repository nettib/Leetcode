class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            flag = 0
            a = nums2.index(num)
            for i in range(a,len(nums2)):
                if nums2[i] > num:
                    ans.append(nums2[i])
                    flag = 1
                    break
            if flag == 0:
                ans.append(-1)
        return ans

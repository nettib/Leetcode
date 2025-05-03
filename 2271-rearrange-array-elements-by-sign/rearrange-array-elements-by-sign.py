class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = n = 0
        ans = []
        while nums[p] < 0:
            p += 1
        while nums[n] > 0:
            n += 1
        while p < len(nums) or n < len(nums):
            if len(ans) == 0 or ans[len(ans) - 1] < 0:
                ans.append(nums[p])
                p += 1 
                while p < len(nums) and nums[p] < 0:
                    p += 1
            else:
                ans.append(nums[n])
                n += 1
                while n < len(nums) and nums[n] > 0:
                    n += 1
        return ans 

        
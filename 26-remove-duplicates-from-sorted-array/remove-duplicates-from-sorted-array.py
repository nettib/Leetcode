class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        p2 = p1 + 1
        k = 1
        while p2 < len(nums):
            if nums[p1] in nums[:p1]:
                if nums[p2] not in nums[:p1]:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1+=1
                    p2 = p2 + 1
                    k+=1
                else:
                    p2+=1
            else:
                p1+=1
                p2 = p1 + 1
                k+=1
        if p1 == len(nums) - 1  and nums[p1] not in nums[:p1]:
            k+=1 
        return k

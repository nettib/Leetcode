class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(l+1, len(nums)):
            if nums[l] == nums[r]:
                nums[l]*=2
                nums[r] = 0
            l+=1
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        return nums
            # for i in range(len(nums) - 1):
            #     if nums[i] == nums[i + 1]:
            #         nums[i] = nums[i] * 2
            #         nums[i + 1] = 0
            # nonZero=[]
            # zero=0
            # for itm in nums:
            #     if itm!=0:
            #         nonZero.append(itm)
            #     else:
            #         zero+=1
            # nonZero.extend([0]*zero)
            # return nonZero
            
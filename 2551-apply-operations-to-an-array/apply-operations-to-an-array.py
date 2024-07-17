class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    nums[i] = nums[i] * 2
                    nums[i + 1] = 0
            nonZero=[]
            zero=0
            for itm in nums:
                if itm!=0:
                    nonZero.append(itm)
                else:
                    zero+=1
            nonZero.extend([0]*zero)
            return nonZero
            
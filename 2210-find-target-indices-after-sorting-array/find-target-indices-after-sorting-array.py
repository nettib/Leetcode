class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size=len(nums)
        for i in range(1,size):
            key=nums[i]
            j=i-1
            while j>=0 and key<nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        target_index=[]
        for s in range(size):
            if nums[s]==target:
                target_index.append(s)
        return target_index


        
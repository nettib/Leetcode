class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newArray=[]
        start=0
        for end in range(len(nums)):
            newArray.append(sum(nums[start:end+1]))
        return newArray
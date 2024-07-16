import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for k in count.keys():
            if count[k]>len(nums)//2:
                return k
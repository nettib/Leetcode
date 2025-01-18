class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        container = {}
        for num in nums:
            if num in container:
                container[num]+=1
            else:
                container[num] = 1
        for num in container:
            if container[num] == 1:
                return num
        

        
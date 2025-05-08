class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in dic:
                count += dic[nums[i]]
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        
        return count 
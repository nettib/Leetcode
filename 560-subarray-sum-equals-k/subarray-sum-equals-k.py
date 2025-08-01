class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = { 0 : 1 }
        res = 0

        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in count:
                res += count[prefix - k]
            count[prefix] = count.get(prefix, 0) + 1
        
        return res
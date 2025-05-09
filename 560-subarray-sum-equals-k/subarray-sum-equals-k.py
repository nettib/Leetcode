from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        total = res = 0
        for num in nums:
            total += num
            res += prefix[total - k]
            prefix[total] += 1
        return res

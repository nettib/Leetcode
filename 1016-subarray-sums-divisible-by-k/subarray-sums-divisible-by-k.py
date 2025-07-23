class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        res = 0

        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k
            if rem in count:
                res += count[rem]
            count[rem] = count.get(rem, 0) + 1

        return res
                
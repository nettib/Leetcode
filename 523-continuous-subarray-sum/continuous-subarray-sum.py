class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0: -1}
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            rem = curr_sum % k
            if rem in prefix:
                if i - prefix[rem] >= 2:
                    return True
            else:
                prefix[rem] = i
        return False